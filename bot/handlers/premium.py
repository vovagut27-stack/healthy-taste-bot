from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from bot.database.db import Database
from bot.keyboards.inline import premium_kb
from bot.services.premium import premium_status_text

router = Router()


async def _send_premium_status(message: Message, db: Database) -> None:
    user = message.from_user
    await db.ensure_user(user.id, user.username, user.full_name)
    is_premium = await db.is_premium(user.id)
    await message.answer(
        premium_status_text(is_premium),
        reply_markup=premium_kb(is_premium),
        parse_mode="HTML",
        disable_web_page_preview=True,
    )


@router.message(F.text.in_({"💎 Премиум", "☕ Поддержать автора"}))
@router.message(Command("premium"))
async def show_premium(message: Message, db: Database) -> None:
    await _send_premium_status(message, db)


@router.callback_query(F.data == "premium:check")
async def check_premium(callback: CallbackQuery, db: Database) -> None:
    await callback.answer()
    user = callback.from_user
    await db.ensure_user(user.id, user.username, user.full_name)
    is_premium = await db.is_premium(user.id)
    if callback.message:
        await callback.message.answer(
            premium_status_text(is_premium),
            reply_markup=premium_kb(is_premium),
            parse_mode="HTML",
            disable_web_page_preview=True,
        )
