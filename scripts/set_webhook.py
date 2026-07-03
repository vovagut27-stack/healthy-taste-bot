"""Установить Telegram webhook после деплоя на Vercel."""
import asyncio
import os
import sys

from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()


async def main() -> None:
    token = os.getenv("BOT_TOKEN")
    webhook_base = os.getenv("WEBHOOK_URL") or os.getenv("VERCEL_URL")

    if not token:
        print("Ошибка: укажите BOT_TOKEN в .env", file=sys.stderr)
        sys.exit(1)
    if not webhook_base:
        print("Ошибка: укажите WEBHOOK_URL или VERCEL_URL", file=sys.stderr)
        sys.exit(1)

    url = webhook_base.rstrip("/")
    if not url.startswith("http"):
        url = f"https://{url}"
    webhook_url = f"{url}/api/webhook"

    bot = Bot(token=token)
    await bot.set_webhook(webhook_url)
    info = await bot.get_webhook_info()
    print(f"Webhook установлен: {info.url}")
    await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
