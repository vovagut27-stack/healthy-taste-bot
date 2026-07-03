import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Config:
    bot_token: str
    db_path: str = "data/bot.db"

    @classmethod
    def from_env(cls) -> "Config":
        token = os.getenv("BOT_TOKEN", "")
        if not token:
            raise ValueError(
                "BOT_TOKEN не найден. Создайте файл .env и укажите токен бота."
            )
        default_db = "/tmp/healthy-taste-bot.db" if os.getenv("VERCEL") else "data/bot.db"
        db_path = os.getenv("DB_PATH", default_db)
        return cls(bot_token=token, db_path=db_path)
