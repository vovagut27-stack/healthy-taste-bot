from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.database.db import Database
from bot.keyboards.inline import (
    categories_kb,
    favorites_kb,
    recipe_actions_kb,
    recipe_list_kb,
)
from bot.keyboards.reply import main_menu_kb
from bot.services.formatter import format_recipe, format_recipe_short
from bot.services.recipes import (
    MEAL_LABELS,
    filter_recipes,
    get_random_recipe,
    get_recipe_by_id,
)
from bot.states.states import IngredientSearch
from bot.keyboards.reply import cancel_kb

router = Router()

NO_RECIPES = (
    "😔 К сожалению, рецептов по этому запросу не найдено.\n"
    "Попробуйте другую категорию или измените настройки в ⚙️ Настройки."
)


async def _send_recipe(message: Message, db: Database, recipe_id: str) -> None:
    recipe = get_recipe_by_id(recipe_id)
    if not recipe:
        await message.answer("Рецепт не найден.")
        return
    is_fav = await db.is_favorite(message.from_user.id, recipe_id)
    text = format_recipe(recipe, is_favorite=is_fav)
    await message.answer(
        text,
        reply_markup=recipe_actions_kb(recipe_id, is_fav),
        parse_mode="HTML",
    )


async def _send_random(message: Message, db: Database) -> None:
    prefs = await db.get_preferences(message.from_user.id)
    recipe = get_random_recipe(
        diet=prefs["diet"],
        goal=prefs["goal"],
        max_time=prefs["max_cook_time"],
    )
    if not recipe:
        await message.answer(NO_RECIPES, reply_markup=main_menu_kb())
        return
    is_fav = await db.is_favorite(message.from_user.id, recipe.id)
    await message.answer(
        format_recipe(recipe, is_favorite=is_fav),
        reply_markup=recipe_actions_kb(recipe.id, is_fav),
        parse_mode="HTML",
    )


@router.message(F.text == "🍳 Найти рецепт")
async def find_recipe(message: Message) -> None:
    await message.answer(
        "Выберите категорию или способ поиска:",
        reply_markup=categories_kb(),
    )


@router.message(F.text == "🎲 Случайный рецепт")
@router.message(Command("random"))
async def random_recipe(message: Message, db: Database) -> None:
    await _send_random(message, db)


@router.message(F.text == "⭐ Избранное")
async def show_favorites(message: Message, db: Database) -> None:
    fav_ids = await db.get_favorites(message.from_user.id)
    if not fav_ids:
        await message.answer(
            "У вас пока нет избранных рецептов.\n"
            "Нажмите ⭐ <b>В избранное</b> под любым рецептом!",
            parse_mode="HTML",
        )
        return
    recipes = []
    for rid in fav_ids:
        r = get_recipe_by_id(rid)
        if r:
            recipes.append((r.id, r.title))
    await message.answer(
        f"<b>⭐ Избранные рецепты ({len(recipes)})</b>",
        reply_markup=favorites_kb(recipes),
        parse_mode="HTML",
    )


@router.callback_query(F.data.startswith("cat:"))
async def category_selected(callback: CallbackQuery, state: FSMContext, db: Database) -> None:
    cat = callback.data.split(":")[1]
    await callback.answer()

    if cat == "ingredients":
        await state.set_state(IngredientSearch.waiting_for_ingredients)
        await callback.message.answer(
            "🥕 Напишите, какие продукты есть дома через запятую.\n"
            "Например: <i>курица, рис, овощи, авокадо</i>",
            reply_markup=cancel_kb(),
            parse_mode="HTML",
        )
        return

    prefs = await db.get_preferences(callback.from_user.id)

    if cat == "fast":
        recipes = filter_recipes(
            diet=prefs["diet"],
            goal=prefs["goal"],
            max_time="fast",
        )
        title = "⚡ Быстрые рецепты (≤20 мин)"
    else:
        recipes = filter_recipes(
            meal_type=cat,
            diet=prefs["diet"],
            goal=prefs["goal"],
        )
        title = MEAL_LABELS.get(cat, cat)

    if not recipes:
        await callback.message.answer(NO_RECIPES)
        return

    if len(recipes) == 1:
        await _send_recipe(callback.message, db, recipes[0].id)
        return

    items = [(r.id, f"{r.emoji} {r.title}") for r in recipes]
    await callback.message.answer(
        f"<b>{title}</b>\nВыберите рецепт:",
        reply_markup=recipe_list_kb(items),
        parse_mode="HTML",
    )


@router.message(IngredientSearch.waiting_for_ingredients, F.text == "❌ Отмена")
async def cancel_ingredients(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer("Поиск отменён.", reply_markup=main_menu_kb())


@router.message(IngredientSearch.waiting_for_ingredients)
async def search_by_ingredients(message: Message, state: FSMContext, db: Database) -> None:
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
            f"По продуктам «{message.text}» точного совпадения нет, "
            "но вот похожие рецепты:",
            reply_markup=main_menu_kb(),
        )
        recipes = filter_recipes(diet=prefs["diet"])[:5]

    if len(recipes) == 1:
        await _send_recipe(message, db, recipes[0].id)
        return

    items = [(r.id, f"{r.emoji} {r.title}") for r in recipes[:10]]
    await message.answer(
        f"🥕 Найдено рецептов: {len(recipes)}\nВыберите:",
        reply_markup=recipe_list_kb(items),
        parse_mode="HTML",
    )


@router.callback_query(F.data.startswith("recipe:"))
async def show_recipe(callback: CallbackQuery, db: Database) -> None:
    recipe_id = callback.data.split(":")[1]
    await callback.answer()
    await _send_recipe(callback.message, db, recipe_id)


@router.callback_query(F.data == "random")
async def callback_random(callback: CallbackQuery, db: Database) -> None:
    await callback.answer()
    await _send_random(callback.message, db)


@router.callback_query(F.data.startswith("fav_add:"))
async def add_favorite(callback: CallbackQuery, db: Database) -> None:
    recipe_id = callback.data.split(":")[1]
    added = await db.add_favorite(callback.from_user.id, recipe_id)
    recipe = get_recipe_by_id(recipe_id)
    if added and recipe:
        await callback.answer(f"⭐ «{recipe.title}» добавлен в избранное!")
    else:
        await callback.answer("Уже в избранном")
    is_fav = True
    await callback.message.edit_reply_markup(
        reply_markup=recipe_actions_kb(recipe_id, is_fav)
    )


@router.callback_query(F.data.startswith("fav_remove:"))
async def remove_favorite(callback: CallbackQuery, db: Database) -> None:
    recipe_id = callback.data.split(":")[1]
    await db.remove_favorite(callback.from_user.id, recipe_id)
    await callback.answer("Удалено из избранного")
    await callback.message.edit_reply_markup(
        reply_markup=recipe_actions_kb(recipe_id, False)
    )


@router.callback_query(F.data == "back_categories")
async def back_categories(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.answer(
        "Выберите категорию:",
        reply_markup=categories_kb(),
    )


@router.callback_query(F.data == "back_main")
async def back_main(callback: CallbackQuery) -> None:
    await callback.answer()


MENU_BUTTONS = {
    "🍳 Найти рецепт", "🎲 Случайный рецепт", "📅 Меню на день",
    "📆 Меню на неделю", "⭐ Избранное", "⚙️ Настройки",
    "💡 Советы по питанию", "❓ Помощь", "❌ Отмена",
}


@router.message(F.text, ~F.text.in_(MENU_BUTTONS), ~F.text.startswith("/"))
async def free_text_search(message: Message, db: Database, state: FSMContext) -> None:
    """Обработка свободного текста — поиск по ингредиентам или ключевым словам."""
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
            "Попробуйте написать продукты через запятую 🥕",
            "Или нажмите 🍳 <b>Найти рецепт</b> для выбора категории",
            "Команда /random — случайный рецепт с вашими настройками",
        ]
        await message.answer(
            f"Не нашёл рецепт по запросу «{message.text}».\n\n"
            + "\n".join(f"• {t}" for t in tips),
            parse_mode="HTML",
        )
        return

    if len(recipes) == 1:
        await _send_recipe(message, db, recipes[0].id)
        return

    items = [(r.id, f"{r.emoji} {r.title}") for r in recipes[:10]]
    await message.answer(
        f"🔍 Найдено {len(recipes)} рецептов по вашему запросу:",
        reply_markup=recipe_list_kb(items),
        parse_mode="HTML",
    )
