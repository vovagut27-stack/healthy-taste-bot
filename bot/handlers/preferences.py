from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from bot.database.db import Database
from bot.keyboards.inline import preferences_kb, pref_diet_kb, pref_goal_kb, pref_time_kb
from bot.services.recipes import DIET_LABELS, GOAL_LABELS, TIME_LABELS

router = Router()


def _format_prefs(prefs: dict) -> str:
    return (
        "<b>⚙️ Ваши настройки</b>\n\n"
        f"🥗 <b>Тип питания:</b> {DIET_LABELS.get(prefs['diet'], prefs['diet'])}\n"
        f"🎯 <b>Цель:</b> {GOAL_LABELS.get(prefs['goal'], prefs['goal'])}\n"
        f"⏱ <b>Время готовки:</b> {TIME_LABELS.get(prefs['max_cook_time'], prefs['max_cook_time'])}\n\n"
        "Эти настройки учитываются при подборе рецептов и составлении меню."
    )


@router.message(F.text == "⚙️ Настройки")
@router.message(Command("preferences"))
async def show_preferences(message: Message, db: Database) -> None:
    prefs = await db.get_preferences(message.from_user.id)
    await message.answer(
        _format_prefs(prefs),
        reply_markup=preferences_kb(),
        parse_mode="HTML",
    )


@router.callback_query(F.data == "pref:diet")
async def pref_diet(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.edit_text(
        "🥗 Выберите тип питания:",
        reply_markup=pref_diet_kb(),
    )


@router.callback_query(F.data == "pref:goal")
async def pref_goal(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.edit_text(
        "🎯 Выберите цель:",
        reply_markup=pref_goal_kb(),
    )


@router.callback_query(F.data == "pref:time")
async def pref_time(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.edit_text(
        "⏱ Выберите предпочитаемое время готовки:",
        reply_markup=pref_time_kb(),
    )


@router.callback_query(F.data == "pref:back")
async def pref_back(callback: CallbackQuery, db: Database) -> None:
    await callback.answer()
    prefs = await db.get_preferences(callback.from_user.id)
    await callback.message.edit_text(
        _format_prefs(prefs),
        reply_markup=preferences_kb(),
        parse_mode="HTML",
    )


@router.callback_query(F.data.startswith("set_diet:"))
async def set_diet(callback: CallbackQuery, db: Database) -> None:
    value = callback.data.split(":")[1]
    await db.update_preference(callback.from_user.id, "diet", value)
    await callback.answer(f"✅ {DIET_LABELS.get(value, value)}")
    prefs = await db.get_preferences(callback.from_user.id)
    await callback.message.edit_text(
        _format_prefs(prefs),
        reply_markup=preferences_kb(),
        parse_mode="HTML",
    )


@router.callback_query(F.data.startswith("set_goal:"))
async def set_goal(callback: CallbackQuery, db: Database) -> None:
    value = callback.data.split(":")[1]
    await db.update_preference(callback.from_user.id, "goal", value)
    await callback.answer(f"✅ {GOAL_LABELS.get(value, value)}")
    prefs = await db.get_preferences(callback.from_user.id)
    await callback.message.edit_text(
        _format_prefs(prefs),
        reply_markup=preferences_kb(),
        parse_mode="HTML",
    )


@router.callback_query(F.data.startswith("set_time:"))
async def set_time(callback: CallbackQuery, db: Database) -> None:
    value = callback.data.split(":")[1]
    await db.update_preference(callback.from_user.id, "max_cook_time", value)
    await callback.answer(f"✅ {TIME_LABELS.get(value, value)}")
    prefs = await db.get_preferences(callback.from_user.id)
    await callback.message.edit_text(
        _format_prefs(prefs),
        reply_markup=preferences_kb(),
        parse_mode="HTML",
    )
