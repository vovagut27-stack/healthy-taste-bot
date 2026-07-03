from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.database.db import Database
from bot.i18n import (
    all_menu_buttons,
    get_meal_labels,
    is_btn,
    is_cancel,
    localized_title,
    t,
)
from bot.keyboards.inline import (
    categories_kb,
    favorites_kb,
    recipe_actions_kb,
    recipe_list_kb,
)
from bot.keyboards.reply import cancel_kb, main_menu_kb
from bot.services.formatter import format_recipe
from bot.services.recipes import filter_recipes, get_random_recipe, get_recipe_by_id
from bot.states.states import IngredientSearch

router = Router()


async def _send_recipe(
    message: Message, db: Database, recipe_id: str, lang: str
) -> None:
    recipe = get_recipe_by_id(recipe_id)
    if not recipe:
        await message.answer(t(lang, "recipes.not_found"))
        return
    is_fav = await db.is_favorite(message.from_user.id, recipe_id)
    text = format_recipe(recipe, is_favorite=is_fav, lang=lang)
    await message.answer(
        text,
        reply_markup=recipe_actions_kb(recipe_id, is_fav, lang),
        parse_mode="HTML",
    )


async def _send_random(message: Message, db: Database, lang: str) -> None:
    user = message.from_user
    await db.ensure_user(user.id, user.username, user.full_name)
    prefs = await db.get_preferences(user.id)
    recipe = get_random_recipe(
        diet=prefs["diet"],
        goal=prefs["goal"],
        max_time=prefs["max_cook_time"],
    )
    if not recipe:
        await message.answer(t(lang, "recipes.no_results"), reply_markup=main_menu_kb(lang))
        return
    is_fav = await db.is_favorite(message.from_user.id, recipe.id)
    await message.answer(
        format_recipe(recipe, is_favorite=is_fav, lang=lang),
        reply_markup=recipe_actions_kb(recipe.id, is_fav, lang),
        parse_mode="HTML",
    )


@router.message(F.func(lambda m: is_btn(m.text, "find_recipe")))
async def find_recipe(message: Message, lang: str) -> None:
    await message.answer(
        t(lang, "recipes.choose_category"),
        reply_markup=categories_kb(lang),
    )


@router.message(F.func(lambda m: is_btn(m.text, "random_recipe")))
@router.message(Command("random"))
async def random_recipe(message: Message, db: Database, lang: str) -> None:
    await _send_random(message, db, lang)


@router.message(F.func(lambda m: is_btn(m.text, "favorites")))
async def show_favorites(message: Message, db: Database, lang: str) -> None:
    fav_ids = await db.get_favorites(message.from_user.id)
    if not fav_ids:
        await message.answer(
            t(lang, "recipes.favorites_empty"),
            parse_mode="HTML",
        )
        return
    recipes = []
    for rid in fav_ids:
        r = get_recipe_by_id(rid)
        if r:
            recipes.append((r.id, f"{r.emoji} {localized_title(r, lang)}"))
    await message.answer(
        t(lang, "recipes.favorites_title", count=len(recipes)),
        reply_markup=favorites_kb(recipes, lang),
        parse_mode="HTML",
    )


@router.callback_query(F.data.startswith("cat:"))
async def category_selected(
    callback: CallbackQuery, state: FSMContext, db: Database, lang: str
) -> None:
    cat = callback.data.split(":")[1]
    await callback.answer()
    user = callback.from_user
    await db.ensure_user(user.id, user.username, user.full_name)

    if cat == "ingredients":
        await state.set_state(IngredientSearch.waiting_for_ingredients)
        await callback.message.answer(
            t(lang, "recipes.ingredients_prompt"),
            reply_markup=cancel_kb(lang),
            parse_mode="HTML",
        )
        return

    prefs = await db.get_preferences(user.id)
    meal_labels = get_meal_labels(lang)

    if cat == "fast":
        recipes = filter_recipes(
            diet=prefs["diet"],
            goal=prefs["goal"],
            max_time="fast",
        )
        title = t(lang, "recipes.fast_title")
    else:
        recipes = filter_recipes(
            meal_type=cat,
            diet=prefs["diet"],
            goal=prefs["goal"],
        )
        title = meal_labels.get(cat, cat)

    if not recipes:
        await callback.message.answer(t(lang, "recipes.no_results"))
        return

    if len(recipes) == 1:
        await _send_recipe(callback.message, db, recipes[0].id, lang)
        return

    items = [(r.id, f"{r.emoji} {localized_title(r, lang)}") for r in recipes]
    await callback.message.answer(
        f"<b>{title}</b>\n{t(lang, 'recipes.choose_recipe')}",
        reply_markup=recipe_list_kb(items, lang),
        parse_mode="HTML",
    )


@router.message(IngredientSearch.waiting_for_ingredients, F.func(lambda m: is_cancel(m.text)))
async def cancel_ingredients(message: Message, state: FSMContext, lang: str) -> None:
    await state.clear()
    await message.answer(t(lang, "recipes.search_cancelled"), reply_markup=main_menu_kb(lang))


@router.message(IngredientSearch.waiting_for_ingredients)
async def search_by_ingredients(
    message: Message, state: FSMContext, db: Database, lang: str
) -> None:
    ingredients = [i.strip() for i in message.text.replace(";", ",").split(",")]
    prefs = await db.get_preferences(message.from_user.id)
    recipes = filter_recipes(
        diet=prefs["diet"],
        goal=prefs["goal"],
        ingredients=ingredients,
    )
    await state.clear()

    if not recipes:
        await message.answer(
            t(lang, "recipes.no_exact_match", query=message.text),
            reply_markup=main_menu_kb(lang),
        )
        recipes = filter_recipes(diet=prefs["diet"])[:5]

    if len(recipes) == 1:
        await _send_recipe(message, db, recipes[0].id, lang)
        return

    items = [(r.id, f"{r.emoji} {localized_title(r, lang)}") for r in recipes[:10]]
    await message.answer(
        t(lang, "recipes.found_count", count=len(recipes)),
        reply_markup=recipe_list_kb(items, lang),
        parse_mode="HTML",
    )


@router.callback_query(F.data.startswith("recipe:"))
async def show_recipe(callback: CallbackQuery, db: Database, lang: str) -> None:
    recipe_id = callback.data.split(":")[1]
    await callback.answer()
    await _send_recipe(callback.message, db, recipe_id, lang)


@router.callback_query(F.data == "random")
async def callback_random(callback: CallbackQuery, db: Database, lang: str) -> None:
    await callback.answer()
    await _send_random(callback.message, db, lang)


@router.callback_query(F.data.startswith("fav_add:"))
async def add_favorite(callback: CallbackQuery, db: Database, lang: str) -> None:
    recipe_id = callback.data.split(":")[1]
    added = await db.add_favorite(callback.from_user.id, recipe_id)
    recipe = get_recipe_by_id(recipe_id)
    if added and recipe:
        await callback.answer(
            t(lang, "recipes.fav_added", title=localized_title(recipe, lang))
        )
    else:
        await callback.answer(t(lang, "recipes.fav_exists"))
    await callback.message.edit_reply_markup(
        reply_markup=recipe_actions_kb(recipe_id, True, lang)
    )


@router.callback_query(F.data.startswith("fav_remove:"))
async def remove_favorite(callback: CallbackQuery, db: Database, lang: str) -> None:
    recipe_id = callback.data.split(":")[1]
    await db.remove_favorite(callback.from_user.id, recipe_id)
    await callback.answer(t(lang, "recipes.fav_removed"))
    await callback.message.edit_reply_markup(
        reply_markup=recipe_actions_kb(recipe_id, False, lang)
    )


@router.callback_query(F.data == "back_categories")
async def back_categories(callback: CallbackQuery, lang: str) -> None:
    await callback.answer()
    await callback.message.answer(
        t(lang, "recipes.choose_category_short"),
        reply_markup=categories_kb(lang),
    )


@router.callback_query(F.data == "back_main")
async def back_main(callback: CallbackQuery) -> None:
    await callback.answer()


@router.message(F.text, ~F.text.in_(all_menu_buttons()), ~F.text.startswith("/"))
async def free_text_search(
    message: Message, db: Database, state: FSMContext, lang: str
) -> None:
    current = await state.get_state()
    if current is not None:
        return

    prefs = await db.get_preferences(message.from_user.id)
    ingredients = [i.strip() for i in message.text.replace(";", ",").split(",")]
    recipes = filter_recipes(
        diet=prefs["diet"],
        goal=prefs["goal"],
        ingredients=ingredients,
    )

    if not recipes:
        tips = [
            t(lang, "recipes.search_tip_1"),
            t(lang, "recipes.search_tip_2"),
            t(lang, "recipes.search_tip_3"),
        ]
        await message.answer(
            t(lang, "recipes.search_not_found", query=message.text)
            + "\n".join(f"• {tip}" for tip in tips),
            parse_mode="HTML",
        )
        return

    if len(recipes) == 1:
        await _send_recipe(message, db, recipes[0].id, lang)
        return

    items = [(r.id, f"{r.emoji} {localized_title(r, lang)}") for r in recipes[:10]]
    await message.answer(
        t(lang, "recipes.search_found", count=len(recipes)),
        reply_markup=recipe_list_kb(items, lang),
        parse_mode="HTML",
    )
