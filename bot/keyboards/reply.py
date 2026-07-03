from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from bot.i18n import btn, t


def main_menu_kb(lang: str = "ru") -> ReplyKeyboardMarkup:
    rows = [
        [btn(lang, "find_recipe"), btn(lang, "random_recipe")],
        [btn(lang, "menu_day"), btn(lang, "menu_week")],
        [btn(lang, "favorites"), btn(lang, "settings")],
        [btn(lang, "premium"), btn(lang, "support")],
        [btn(lang, "tips"), btn(lang, "help")],
    ]
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=b) for b in row] for row in rows],
        resize_keyboard=True,
        input_field_placeholder=t(lang, "keyboard.placeholder"),
    )


def cancel_kb(lang: str = "ru") -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=btn(lang, "cancel"))]],
        resize_keyboard=True,
    )
