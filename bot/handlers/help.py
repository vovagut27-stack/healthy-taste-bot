import random

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.i18n import get_list, is_btn, t

router = Router()


@router.message(F.func(lambda m: is_btn(m.text, "help")))
@router.message(Command("help"))
async def cmd_help(message: Message, lang: str) -> None:
    await message.answer(t(lang, "help.text"), parse_mode="HTML")


@router.message(F.func(lambda m: is_btn(m.text, "tips")))
async def nutrition_tips(message: Message, lang: str) -> None:
    tip = random.choice(get_list(lang, "tips.items"))
    await message.answer(
        t(lang, "tips.title", tip=tip),
        parse_mode="HTML",
    )
