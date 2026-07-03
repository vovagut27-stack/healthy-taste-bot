from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message, TelegramObject

from bot.database.db import Database
from bot.i18n import DEFAULT_LANG, SUPPORTED_LANGS


class LanguageMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        db: Database | None = data.get("db")
        lang = DEFAULT_LANG

        user_id = None
        if isinstance(event, Message) and event.from_user:
            user_id = event.from_user.id
        elif isinstance(event, CallbackQuery) and event.from_user:
            user_id = event.from_user.id

        if db and user_id:
            prefs = await db.get_preferences(user_id)
            candidate = prefs.get("language", DEFAULT_LANG)
            lang = candidate if candidate in SUPPORTED_LANGS else DEFAULT_LANG

        data["lang"] = lang
        return await handler(event, data)
