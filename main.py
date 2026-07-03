import asyncio
import logging
import sys

from bot.app import create_bot_and_dispatcher
from config import Config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)


async def main() -> None:
    config = Config.from_env()
    bot, dp, db = create_bot_and_dispatcher(config)
    await db.init()

    logger.info("Бот «Здоровый Вкус» запущен (polling)")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен")
