from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

MAIN_MENU_BUTTONS = [
    ["🍳 Найти рецепт", "🎲 Случайный рецепт"],
    ["📅 Меню на день", "📆 Меню на неделю"],
    ["⭐ Избранное", "⚙️ Настройки"],
    ["💡 Советы по питанию", "❓ Помощь"],
]

MEAL_TYPE_BUTTONS = [
    ["🌅 Завтрак", "☀️ Обед", "🌙 Ужин"],
    ["🍎 Перекус", "🍰 Десерт", "🔙 Назад"],
]

DIET_BUTTONS = [
    ["ПП", "Кето", "Низкоуглеводное"],
    ["Веган", "Вегетарианское"],
    ["Без глютена", "Без лактозы", "Любая"],
    ["🔙 Назад"],
]

TIME_BUTTONS = [
    ["⚡ Быстро (≤20 мин)", "🕐 Средне"],
    ["🕰 Долго", "Любое время", "🔙 Назад"],
]

GOAL_BUTTONS = [
    ["Похудение", "Набор массы"],
    ["Поддержание", "Детокс", "🔙 Назад"],
]

CANCEL_BUTTON = KeyboardButton(text="❌ Отмена")


def main_menu_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=b) for b in row] for row in MAIN_MENU_BUTTONS],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие или напишите запрос...",
    )


def meal_type_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=b) for b in row] for row in MEAL_TYPE_BUTTONS],
        resize_keyboard=True,
    )


def diet_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=b) for b in row] for row in DIET_BUTTONS],
        resize_keyboard=True,
    )


def time_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=b) for b in row] for row in TIME_BUTTONS],
        resize_keyboard=True,
    )


def goal_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=b) for b in row] for row in GOAL_BUTTONS],
        resize_keyboard=True,
    )


def cancel_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[CANCEL_BUTTON]],
        resize_keyboard=True,
    )


MEAL_TEXT_TO_KEY = {
    "🌅 Завтрак": "breakfast",
    "☀️ Обед": "lunch",
    "🌙 Ужин": "dinner",
    "🍎 Перекус": "snack",
    "🍰 Десерт": "dessert",
}

DIET_TEXT_TO_KEY = {
    "ПП": "pp",
    "Кето": "keto",
    "Низкоуглеводное": "low_carb",
    "Веган": "vegan",
    "Вегетарианское": "vegetarian",
    "Без глютена": "gluten_free",
    "Без лактозы": "lactose_free",
    "Любая": "any",
}

TIME_TEXT_TO_KEY = {
    "⚡ Быстро (≤20 мин)": "fast",
    "🕐 Средне": "medium",
    "🕰 Долго": "long",
    "Любое время": "any",
}

GOAL_TEXT_TO_KEY = {
    "Похудение": "weight_loss",
    "Набор массы": "muscle_gain",
    "Поддержание": "maintain",
    "Детокс": "detox",
}
