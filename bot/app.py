import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from bot.database.db import Database
from bot.handlers import help, menu, preferences, recipes, start
from bot.middlewares.db import DatabaseMiddleware
from config import Config


def create_bot_and_dispatcher(config: Config | None = None) -> tuple[Bot, Dispatcher, Database]:
    config = config or Config.from_env()
    db_dir = os.path.dirname(config.db_path)
    if db_dir and db_dir not in (".", "/tmp"):
        os.makedirs(db_dir, exist_ok=True)

    db = Database(config.db_path)
    bot = Bot(
        token=config.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(storage=MemoryStorage())
    dp.update.middleware(DatabaseMiddleware(db))

    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(preferences.router)
    dp.include_router(help.router)
    dp.include_router(recipes.router)

    return bot, dp, db
