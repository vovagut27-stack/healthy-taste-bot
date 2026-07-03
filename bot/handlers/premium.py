from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from bot.database.db import Database
from bot.i18n import is_btn, t
from bot.keyboards.inline import premium_kb
from bot.services.premium import premium_status_text

router = Router()


async def _send_premium_status(message: Message, db: Database, lang: str) -> None:
    user = message.from_user
    await db.ensure_user(user.id, user.username, user.full_name)
    is_premium = await db.is_premium(user.id)
    await message.answer(
        premium_status_text(is_premium, lang),
        reply_markup=premium_kb(is_premium, lang),
        parse_mode="HTML",
        disable_web_page_preview=True,
    )


@router.message(F.func(lambda m: is_btn(m.text, "premium") or is_btn(m.text, "support")))
@router.message(Command("premium"))
async def show_premium(message: Message, db: Database, lang: str) -> None:
    await _send_premium_status(message, db, lang)


@router.callback_query(F.data == "premium:check")
async def check_premium(callback: CallbackQuery, db: Database, lang: str) -> None:
    await callback.answer()
    user = callback.from_user
    await db.ensure_user(user.id, user.username, user.full_name)
    is_premium = await db.is_premium(user.id)
    if callback.message:
        await callback.message.answer(
            premium_status_text(is_premium, lang),
            reply_markup=premium_kb(is_premium, lang),
            parse_mode="HTML",
            disable_web_page_preview=True,
        )
