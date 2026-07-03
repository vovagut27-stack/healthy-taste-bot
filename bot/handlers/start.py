from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.database.db import Database
from bot.keyboards.reply import main_menu_kb
from bot.services.premium import DONATTY_URL
from bot.texts import WELCOME_TEXT

router = Router()


def _welcome_text(is_premium: bool) -> str:
    text = WELCOME_TEXT
    if is_premium:
        text += "\n\n💎 <b>Премиум активен</b> — спасибо за поддержку!"
    else:
        text += (
            f"\n\n☕ Поддержать автора: <a href=\"{DONATTY_URL}\">Donatty</a>"
        )
    return text


@router.message(CommandStart())
async def cmd_start(message: Message, db: Database) -> None:
    user = message.from_user
    await db.ensure_user(user.id, user.username, user.full_name)
    is_premium = await db.is_premium(user.id)
    await message.answer(
        _welcome_text(is_premium),
        reply_markup=main_menu_kb(),
        parse_mode="HTML",
        disable_web_page_preview=True,
    )

