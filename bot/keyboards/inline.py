from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.services.premium import DONATTY_URL


def recipe_actions_kb(recipe_id: str, is_favorite: bool) -> InlineKeyboardMarkup:
    fav_text = "💔 Удалить из избранного" if is_favorite else "⭐ В избранное"
    fav_callback = f"fav_remove:{recipe_id}" if is_favorite else f"fav_add:{recipe_id}"
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=fav_text, callback_data=fav_callback),
                InlineKeyboardButton(text="🎲 Ещё рецепт", callback_data="random"),
            ],
            [
                InlineKeyboardButton(text="🔙 К категориям", callback_data="back_categories"),
            ],
        ]
    )


def recipe_list_kb(recipes: list[tuple[str, str]]) -> InlineKeyboardMarkup:
    """recipes: list of (recipe_id, title)"""
    buttons = [
        [InlineKeyboardButton(text=title, callback_data=f"recipe:{rid}")]
        for rid, title in recipes
    ]
    buttons.append(
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_categories")]
    )
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def categories_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🌅 Завтрак", callback_data="cat:breakfast"),
                InlineKeyboardButton(text="☀️ Обед", callback_data="cat:lunch"),
            ],
            [
                InlineKeyboardButton(text="🌙 Ужин", callback_data="cat:dinner"),
                InlineKeyboardButton(text="🍎 Перекус", callback_data="cat:snack"),
            ],
            [
                InlineKeyboardButton(text="🍰 Десерт", callback_data="cat:dessert"),
                InlineKeyboardButton(text="🥕 По ингредиентам", callback_data="cat:ingredients"),
            ],
            [
                InlineKeyboardButton(text="⚡ Быстрые (≤20 мин)", callback_data="cat:fast"),
            ],
        ]
    )


def menu_type_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📅 На день", callback_data="menu:day"),
                InlineKeyboardButton(text="📆 На неделю", callback_data="menu:week"),
            ],
        ]
    )


def preferences_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🥗 Тип питания", callback_data="pref:diet")],
            [InlineKeyboardButton(text="🎯 Цель", callback_data="pref:goal")],
            [InlineKeyboardButton(text="⏱ Время готовки", callback_data="pref:time")],
        ]
    )


def pref_diet_kb() -> InlineKeyboardMarkup:
    diets = [
        ("ПП", "pp"), ("Кето", "keto"), ("Низкоугл.", "low_carb"),
        ("Веган", "vegan"), ("Вегетар.", "vegetarian"),
        ("Без глютена", "gluten_free"), ("Без лактозы", "lactose_free"),
    ]
    rows = []
    for i in range(0, len(diets), 2):
        row = [
            InlineKeyboardButton(text=label, callback_data=f"set_diet:{key}")
            for label, key in diets[i : i + 2]
        ]
        rows.append(row)
    rows.append([InlineKeyboardButton(text="🔙 Назад", callback_data="pref:back")])
    return InlineKeyboardMarkup(inline_keyboard=rows)


def pref_goal_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Похудение", callback_data="set_goal:weight_loss"),
                InlineKeyboardButton(text="Набор массы", callback_data="set_goal:muscle_gain"),
            ],
            [
                InlineKeyboardButton(text="Поддержание", callback_data="set_goal:maintain"),
                InlineKeyboardButton(text="Детокс", callback_data="set_goal:detox"),
            ],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="pref:back")],
        ]
    )


def pref_time_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="⚡ Быстро", callback_data="set_time:fast"),
                InlineKeyboardButton(text="🕐 Средне", callback_data="set_time:medium"),
            ],
            [
                InlineKeyboardButton(text="🕰 Долго", callback_data="set_time:long"),
                InlineKeyboardButton(text="Любое", callback_data="set_time:any"),
            ],
            [InlineKeyboardButton(text="🔙 Назад", callback_data="pref:back")],
        ]
    )


def favorites_kb(recipes: list[tuple[str, str]]) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text=f"⭐ {title}", callback_data=f"recipe:{rid}")]
        for rid, title in recipes
    ]
    if not buttons:
        buttons = [[InlineKeyboardButton(text="🔙 Назад", callback_data="back_main")]]
    else:
        buttons.append([InlineKeyboardButton(text="🔙 Назад", callback_data="back_main")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def premium_kb(is_premium: bool) -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton(text="☕ Поддержать на Donatty", url=DONATTY_URL)],
    ]
    if not is_premium:
        rows.append(
            [InlineKeyboardButton(text="🔄 Проверить статус", callback_data="premium:check")]
        )
    return InlineKeyboardMarkup(inline_keyboard=rows)
