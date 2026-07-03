import aiosqlite

from bot.services.premium import PREGRANTED_USERNAMES

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    full_name TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS preferences (
    user_id INTEGER PRIMARY KEY,
    diet TEXT DEFAULT 'pp',
    goal TEXT DEFAULT 'maintain',
    max_cook_time TEXT DEFAULT 'any',
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS favorites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    recipe_id TEXT NOT NULL,
    saved_at TEXT DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, recipe_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS premium_grants (
    username TEXT PRIMARY KEY COLLATE NOCASE,
    note TEXT,
    granted_at TEXT DEFAULT CURRENT_TIMESTAMP
);
"""


class Database:
    def __init__(self, db_path: str):
        self.db_path = db_path

    async def init(self) -> None:
        async with aiosqlite.connect(self.db_path) as conn:
            conn.row_factory = aiosqlite.Row
            await conn.executescript(SCHEMA)
            try:
                await conn.execute(
                    "ALTER TABLE users ADD COLUMN is_premium INTEGER NOT NULL DEFAULT 0"
                )
            except aiosqlite.OperationalError:
                pass
            for username in PREGRANTED_USERNAMES:
                await conn.execute(
                    """
                    INSERT OR IGNORE INTO premium_grants (username, note)
                    VALUES (?, 'Выдан автором')
                    """,
                    (username.lower(),),
                )
            await conn.commit()

    async def ensure_user(
        self, user_id: int, username: str | None, full_name: str | None
    ) -> None:
        async with aiosqlite.connect(self.db_path) as conn:
            conn.row_factory = aiosqlite.Row
            await conn.execute(
                """
                INSERT INTO users (user_id, username, full_name)
                VALUES (?, ?, ?)
                ON CONFLICT(user_id) DO UPDATE SET
                    username = excluded.username,
                    full_name = excluded.full_name
                """,
                (user_id, username, full_name),
            )
            await conn.execute(
                """
                INSERT OR IGNORE INTO preferences (user_id)
                VALUES (?)
                """,
                (user_id,),
            )
            await conn.commit()
        if username:
            await self.apply_premium_grant(user_id, username)

    async def apply_premium_grant(self, user_id: int, username: str) -> bool:
        normalized = username.lstrip("@").lower()
        async with aiosqlite.connect(self.db_path) as conn:
            conn.row_factory = aiosqlite.Row
            cursor = await conn.execute(
                "SELECT 1 FROM premium_grants WHERE username = ?",
                (normalized,),
            )
            if await cursor.fetchone() is None:
                return False
            await conn.execute(
                "UPDATE users SET is_premium = 1 WHERE user_id = ?",
                (user_id,),
            )
            await conn.commit()
            return True

    async def is_premium(self, user_id: int) -> bool:
        async with aiosqlite.connect(self.db_path) as conn:
            conn.row_factory = aiosqlite.Row
            cursor = await conn.execute(
                "SELECT is_premium FROM users WHERE user_id = ?",
                (user_id,),
            )
            row = await cursor.fetchone()
            return bool(row and row["is_premium"])

    async def set_premium(self, user_id: int, enabled: bool = True) -> None:
        async with aiosqlite.connect(self.db_path) as conn:
            await conn.execute(
                "UPDATE users SET is_premium = ? WHERE user_id = ?",
                (1 if enabled else 0, user_id),
            )
            await conn.commit()

    async def grant_premium_username(self, username: str, note: str = "") -> None:
        normalized = username.lstrip("@").lower()
        async with aiosqlite.connect(self.db_path) as conn:
            await conn.execute(
                """
                INSERT INTO premium_grants (username, note)
                VALUES (?, ?)
                ON CONFLICT(username) DO UPDATE SET note = excluded.note
                """,
                (normalized, note),
            )
            cursor = await conn.execute(
                "SELECT user_id FROM users WHERE LOWER(username) = ?",
                (normalized,),
            )
            row = await cursor.fetchone()
            if row:
                await conn.execute(
                    "UPDATE users SET is_premium = 1 WHERE user_id = ?",
                    (row["user_id"],),
                )
            await conn.commit()

    async def get_preferences(self, user_id: int) -> dict:
        async with aiosqlite.connect(self.db_path) as conn:
            conn.row_factory = aiosqlite.Row
            cursor = await conn.execute(
                "SELECT diet, goal, max_cook_time FROM preferences WHERE user_id = ?",
                (user_id,),
            )
            row = await cursor.fetchone()
            if row is None:
                return {"diet": "pp", "goal": "maintain", "max_cook_time": "any"}
            return dict(row)

    async def update_preference(
        self, user_id: int, field: str, value: str
    ) -> None:
        allowed = {"diet", "goal", "max_cook_time"}
        if field not in allowed:
            raise ValueError(f"Unknown preference field: {field}")
        async with aiosqlite.connect(self.db_path) as conn:
            await conn.execute(
                f"UPDATE preferences SET {field} = ? WHERE user_id = ?",
                (value, user_id),
            )
            await conn.commit()

    async def add_favorite(self, user_id: int, recipe_id: str) -> bool:
        async with aiosqlite.connect(self.db_path) as conn:
            try:
                await conn.execute(
                    "INSERT INTO favorites (user_id, recipe_id) VALUES (?, ?)",
                    (user_id, recipe_id),
                )
                await conn.commit()
                return True
            except aiosqlite.IntegrityError:
                return False

    async def remove_favorite(self, user_id: int, recipe_id: str) -> None:
        async with aiosqlite.connect(self.db_path) as conn:
            await conn.execute(
                "DELETE FROM favorites WHERE user_id = ? AND recipe_id = ?",
                (user_id, recipe_id),
            )
            await conn.commit()

    async def is_favorite(self, user_id: int, recipe_id: str) -> bool:
        async with aiosqlite.connect(self.db_path) as conn:
            conn.row_factory = aiosqlite.Row
            cursor = await conn.execute(
                "SELECT 1 FROM favorites WHERE user_id = ? AND recipe_id = ?",
                (user_id, recipe_id),
            )
            return await cursor.fetchone() is not None

    async def get_favorites(self, user_id: int) -> list[str]:
        async with aiosqlite.connect(self.db_path) as conn:
            conn.row_factory = aiosqlite.Row
            cursor = await conn.execute(
                "SELECT recipe_id FROM favorites WHERE user_id = ? ORDER BY saved_at DESC",
                (user_id,),
            )
            rows = await cursor.fetchall()
            return [row["recipe_id"] for row in rows]
