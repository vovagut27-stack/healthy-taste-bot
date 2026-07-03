from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.database.db import Database
from bot.i18n import t
from bot.keyboards.reply import main_menu_kb
from bot.services.premium import DONATTY_URL

router = Router()


def _welcome_text(is_premium: bool, lang: str) -> str:
    text = t(lang, "welcome.text")
    if is_premium:
        text += "\n\n" + t(lang, "welcome.premium_active")
    else:
        text += "\n\n" + t(lang, "welcome.support", url=DONATTY_URL)
    return text


@router.message(CommandStart())
async def cmd_start(message: Message, db: Database, lang: str) -> None:
    user = message.from_user
    await db.ensure_user(user.id, user.username, user.full_name)
    is_premium = await db.is_premium(user.id)
    await message.answer(
        _welcome_text(is_premium, lang),
        reply_markup=main_menu_kb(lang),
        parse_mode="HTML",
        disable_web_page_preview=True,
    )
