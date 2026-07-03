from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from bot.database.db import Database
from bot.keyboards.inline import menu_type_kb, premium_kb
from bot.services.formatter import format_daily_menu, format_weekly_menu
from bot.services.premium import premium_required_text
from bot.services.recipes import build_daily_menu, build_weekly_menu

router = Router()


@router.message(F.text == "📆 Меню на неделю")
async def menu_week_prompt(message: Message, db: Database) -> None:
    if not await db.is_premium(message.from_user.id):
        await message.answer(
            premium_required_text(),
            reply_markup=premium_kb(False),
            parse_mode="HTML",
            disable_web_page_preview=True,
        )
        return
    await message.answer("📋 Составляю меню на неделю…")
    prefs = await db.get_preferences(message.from_user.id)
    week = build_weekly_menu(diet=prefs["diet"], goal=prefs["goal"])
    text = format_weekly_menu(week)
    await message.answer(text, parse_mode="HTML")


@router.message(F.text == "📅 Меню на день")
@router.message(Command("menu"))
async def menu_prompt(message: Message) -> None:
    await message.answer(
        "📋 Выберите тип меню:",
        reply_markup=menu_type_kb(),
    )


@router.callback_query(F.data == "menu:day")
async def menu_day(callback: CallbackQuery, db: Database) -> None:
    await callback.answer()
    prefs = await db.get_preferences(callback.from_user.id)
    menu = build_daily_menu(diet=prefs["diet"], goal=prefs["goal"])
    text = format_daily_menu(menu)
    await callback.message.answer(text, parse_mode="HTML")


@router.callback_query(F.data == "menu:week")
async def menu_week(callback: CallbackQuery, db: Database) -> None:
    await callback.answer()
    if not await db.is_premium(callback.from_user.id):
        await callback.message.answer(
            premium_required_text(),
            reply_markup=premium_kb(False),
            parse_mode="HTML",
            disable_web_page_preview=True,
        )
        return
    prefs = await db.get_preferences(callback.from_user.id)
    week = build_weekly_menu(diet=prefs["diet"], goal=prefs["goal"])
    text = format_weekly_menu(week)
    await callback.message.answer(text, parse_mode="HTML")
