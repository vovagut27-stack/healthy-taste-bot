import random

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.texts import HELP_TEXT, NUTRITION_TIPS

router = Router()


@router.message(F.text == "❓ Помощь")
@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(HELP_TEXT, parse_mode="HTML")


@router.message(F.text == "💡 Советы по питанию")
async def nutrition_tips(message: Message) -> None:
    tip = random.choice(NUTRITION_TIPS)
    await message.answer(
        f"<b>💡 Совет дня</b>\n\n{tip}",
        parse_mode="HTML",
    )
