from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.database.db import Database
from bot.keyboards.reply import main_menu_kb
from bot.texts import WELCOME_TEXT

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, db: Database) -> None:
    user = message.from_user
    await db.ensure_user(user.id, user.username, user.full_name)
    await message.answer(WELCOME_TEXT, reply_markup=main_menu_kb(), parse_mode="HTML")

