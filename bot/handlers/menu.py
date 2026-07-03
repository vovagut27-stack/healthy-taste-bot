from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from bot.database.db import Database
from bot.i18n import is_btn, t
from bot.keyboards.inline import menu_type_kb, premium_kb
from bot.services.formatter import format_daily_menu, format_weekly_menu
from bot.services.premium import premium_required_text
from bot.services.recipes import build_daily_menu, build_weekly_menu

router = Router()


@router.message(F.func(lambda m: is_btn(m.text, "menu_week")))
async def menu_week_prompt(message: Message, db: Database, lang: str) -> None:
    user = message.from_user
    await db.ensure_user(user.id, user.username, user.full_name)
    if not await db.is_premium(user.id):
        await message.answer(
            premium_required_text(lang),
            reply_markup=premium_kb(False, lang),
            parse_mode="HTML",
            disable_web_page_preview=True,
        )
        return
    await message.answer(t(lang, "menu.building_week"))
    prefs = await db.get_preferences(message.from_user.id)
    week = build_weekly_menu(diet=prefs["diet"], goal=prefs["goal"])
    text = format_weekly_menu(week, lang)
    await message.answer(text, parse_mode="HTML")


@router.message(F.func(lambda m: is_btn(m.text, "menu_day")))
@router.message(Command("menu"))
async def menu_prompt(message: Message, lang: str) -> None:
    await message.answer(
        t(lang, "menu.choose_type"),
        reply_markup=menu_type_kb(lang),
    )


@router.callback_query(F.data == "menu:day")
async def menu_day(callback: CallbackQuery, db: Database, lang: str) -> None:
    await callback.answer()
    user = callback.from_user
    await db.ensure_user(user.id, user.username, user.full_name)
    prefs = await db.get_preferences(user.id)
    menu = build_daily_menu(diet=prefs["diet"], goal=prefs["goal"])
    text = format_daily_menu(menu, lang)
    await callback.message.answer(text, parse_mode="HTML")


@router.callback_query(F.data == "menu:week")
async def menu_week(callback: CallbackQuery, db: Database, lang: str) -> None:
    await callback.answer()
    user = callback.from_user
    await db.ensure_user(user.id, user.username, user.full_name)
    if not await db.is_premium(user.id):
        await callback.message.answer(
            premium_required_text(lang),
            reply_markup=premium_kb(False, lang),
            parse_mode="HTML",
            disable_web_page_preview=True,
        )
        return
    prefs = await db.get_preferences(user.id)
    week = build_weekly_menu(diet=prefs["diet"], goal=prefs["goal"])
    text = format_weekly_menu(week, lang)
    await callback.message.answer(text, parse_mode="HTML")
