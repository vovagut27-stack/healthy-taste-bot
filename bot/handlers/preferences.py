from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from bot.database.db import Database
from bot.i18n import (
    get_diet_labels,
    get_goal_labels,
    get_time_labels,
    is_btn,
    t,
)
from bot.keyboards.inline import (
    pref_diet_kb,
    pref_goal_kb,
    pref_lang_kb,
    pref_time_kb,
    preferences_kb,
)
from bot.keyboards.reply import main_menu_kb

router = Router()


def _format_prefs(prefs: dict, lang: str) -> str:
    diet_labels = get_diet_labels(lang)
    goal_labels = get_goal_labels(lang)
    time_labels = get_time_labels(lang)
    lang_label = t(lang, f"labels.language.{prefs['language']}")
    return (
        t(lang, "prefs.title")
        + t(lang, "prefs.diet_line", value=diet_labels.get(prefs["diet"], prefs["diet"]))
        + t(lang, "prefs.goal_line", value=goal_labels.get(prefs["goal"], prefs["goal"]))
        + t(
            lang,
            "prefs.time_line",
            value=time_labels.get(prefs["max_cook_time"], prefs["max_cook_time"]),
        )
        + t(lang, "prefs.lang_line", value=lang_label)
        + t(lang, "prefs.footer")
    )


@router.message(F.func(lambda m: is_btn(m.text, "settings")))
@router.message(Command("preferences"))
async def show_preferences(message: Message, db: Database, lang: str) -> None:
    prefs = await db.get_preferences(message.from_user.id)
    await message.answer(
        _format_prefs(prefs, lang),
        reply_markup=preferences_kb(lang),
        parse_mode="HTML",
    )


@router.callback_query(F.data == "pref:diet")
async def pref_diet(callback: CallbackQuery, lang: str) -> None:
    await callback.answer()
    await callback.message.edit_text(
        t(lang, "prefs.choose_diet"),
        reply_markup=pref_diet_kb(lang),
    )


@router.callback_query(F.data == "pref:goal")
async def pref_goal(callback: CallbackQuery, lang: str) -> None:
    await callback.answer()
    await callback.message.edit_text(
        t(lang, "prefs.choose_goal"),
        reply_markup=pref_goal_kb(lang),
    )


@router.callback_query(F.data == "pref:time")
async def pref_time(callback: CallbackQuery, lang: str) -> None:
    await callback.answer()
    await callback.message.edit_text(
        t(lang, "prefs.choose_time"),
        reply_markup=pref_time_kb(lang),
    )


@router.callback_query(F.data == "pref:lang")
async def pref_lang(callback: CallbackQuery, lang: str) -> None:
    await callback.answer()
    await callback.message.edit_text(
        t(lang, "prefs.choose_lang"),
        reply_markup=pref_lang_kb(lang),
    )


@router.callback_query(F.data == "pref:back")
async def pref_back(callback: CallbackQuery, db: Database, lang: str) -> None:
    await callback.answer()
    prefs = await db.get_preferences(callback.from_user.id)
    await callback.message.edit_text(
        _format_prefs(prefs, lang),
        reply_markup=preferences_kb(lang),
        parse_mode="HTML",
    )


@router.callback_query(F.data.startswith("set_diet:"))
async def set_diet(callback: CallbackQuery, db: Database, lang: str) -> None:
    value = callback.data.split(":")[1]
    await db.update_preference(callback.from_user.id, "diet", value)
    diet_labels = get_diet_labels(lang)
    await callback.answer(f"✅ {diet_labels.get(value, value)}")
    prefs = await db.get_preferences(callback.from_user.id)
    await callback.message.edit_text(
        _format_prefs(prefs, lang),
        reply_markup=preferences_kb(lang),
        parse_mode="HTML",
    )


@router.callback_query(F.data.startswith("set_goal:"))
async def set_goal(callback: CallbackQuery, db: Database, lang: str) -> None:
    value = callback.data.split(":")[1]
    await db.update_preference(callback.from_user.id, "goal", value)
    goal_labels = get_goal_labels(lang)
    await callback.answer(f"✅ {goal_labels.get(value, value)}")
    prefs = await db.get_preferences(callback.from_user.id)
    await callback.message.edit_text(
        _format_prefs(prefs, lang),
        reply_markup=preferences_kb(lang),
        parse_mode="HTML",
    )


@router.callback_query(F.data.startswith("set_time:"))
async def set_time(callback: CallbackQuery, db: Database, lang: str) -> None:
    value = callback.data.split(":")[1]
    await db.update_preference(callback.from_user.id, "max_cook_time", value)
    time_labels = get_time_labels(lang)
    await callback.answer(f"✅ {time_labels.get(value, value)}")
    prefs = await db.get_preferences(callback.from_user.id)
    await callback.message.edit_text(
        _format_prefs(prefs, lang),
        reply_markup=preferences_kb(lang),
        parse_mode="HTML",
    )


@router.callback_query(F.data.startswith("set_lang:"))
async def set_language(callback: CallbackQuery, db: Database, lang: str) -> None:
    new_lang = callback.data.split(":")[1]
    await db.update_preference(callback.from_user.id, "language", new_lang)
    lang_label = t(new_lang, f"labels.language.{new_lang}")
    await callback.answer(t(new_lang, "prefs.lang_changed", lang=lang_label))
    prefs = await db.get_preferences(callback.from_user.id)
    await callback.message.edit_text(
        _format_prefs(prefs, new_lang),
        reply_markup=preferences_kb(new_lang),
        parse_mode="HTML",
    )
    await callback.message.answer(
        t(new_lang, "welcome.text"),
        reply_markup=main_menu_kb(new_lang),
        parse_mode="HTML",
    )
