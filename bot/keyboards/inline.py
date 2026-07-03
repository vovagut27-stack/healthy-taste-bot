from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.i18n import get_meal_labels, t
from bot.services.premium import DONATTY_URL


def recipe_actions_kb(recipe_id: str, is_favorite: bool, lang: str = "ru") -> InlineKeyboardMarkup:
    fav_text = t(lang, "keyboard.fav_remove") if is_favorite else t(lang, "keyboard.fav_add")
    fav_callback = f"fav_remove:{recipe_id}" if is_favorite else f"fav_add:{recipe_id}"
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=fav_text, callback_data=fav_callback),
                InlineKeyboardButton(text=t(lang, "keyboard.another"), callback_data="random"),
            ],
            [
                InlineKeyboardButton(
                    text=t(lang, "keyboard.back_categories"),
                    callback_data="back_categories",
                ),
            ],
        ]
    )


def recipe_list_kb(recipes: list[tuple[str, str]], lang: str = "ru") -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text=title, callback_data=f"recipe:{rid}")]
        for rid, title in recipes
    ]
    buttons.append(
        [InlineKeyboardButton(text=t(lang, "keyboard.back"), callback_data="back_categories")]
    )
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def categories_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    meals = get_meal_labels(lang)
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=meals["breakfast"], callback_data="cat:breakfast"),
                InlineKeyboardButton(text=meals["lunch"], callback_data="cat:lunch"),
            ],
            [
                InlineKeyboardButton(text=meals["dinner"], callback_data="cat:dinner"),
                InlineKeyboardButton(text=meals["snack"], callback_data="cat:snack"),
            ],
            [
                InlineKeyboardButton(text=meals["dessert"], callback_data="cat:dessert"),
                InlineKeyboardButton(
                    text=t(lang, "keyboard.by_ingredients"),
                    callback_data="cat:ingredients",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=t(lang, "keyboard.fast_short"),
                    callback_data="cat:fast",
                ),
            ],
        ]
    )


def menu_type_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=t(lang, "keyboard.menu_day_short"),
                    callback_data="menu:day",
                ),
                InlineKeyboardButton(
                    text=t(lang, "keyboard.menu_week_short"),
                    callback_data="menu:week",
                ),
            ],
        ]
    )


def preferences_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=t(lang, "keyboard.pref_diet"), callback_data="pref:diet")],
            [InlineKeyboardButton(text=t(lang, "keyboard.pref_goal"), callback_data="pref:goal")],
            [InlineKeyboardButton(text=t(lang, "keyboard.pref_time"), callback_data="pref:time")],
            [InlineKeyboardButton(text=t(lang, "keyboard.pref_lang"), callback_data="pref:lang")],
        ]
    )


def pref_diet_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    diets = [
        (t(lang, "keyboard.diet_pp"), "pp"),
        (t(lang, "keyboard.diet_keto"), "keto"),
        (t(lang, "keyboard.diet_low_carb"), "low_carb"),
        (t(lang, "keyboard.diet_vegan"), "vegan"),
        (t(lang, "keyboard.diet_veget"), "vegetarian"),
        (t(lang, "keyboard.diet_gluten"), "gluten_free"),
        (t(lang, "keyboard.diet_lactose"), "lactose_free"),
    ]
    rows = []
    for i in range(0, len(diets), 2):
        row = [
            InlineKeyboardButton(text=label, callback_data=f"set_diet:{key}")
            for label, key in diets[i : i + 2]
        ]
        rows.append(row)
    rows.append([InlineKeyboardButton(text=t(lang, "keyboard.back"), callback_data="pref:back")])
    return InlineKeyboardMarkup(inline_keyboard=rows)


def pref_goal_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    goals = [
        ("weight_loss", t(lang, "labels.goal.weight_loss")),
        ("muscle_gain", t(lang, "labels.goal.muscle_gain")),
        ("maintain", t(lang, "labels.goal.maintain")),
        ("detox", t(lang, "labels.goal.detox")),
    ]
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=goals[0][1], callback_data=f"set_goal:{goals[0][0]}"),
                InlineKeyboardButton(text=goals[1][1], callback_data=f"set_goal:{goals[1][0]}"),
            ],
            [
                InlineKeyboardButton(text=goals[2][1], callback_data=f"set_goal:{goals[2][0]}"),
                InlineKeyboardButton(text=goals[3][1], callback_data=f"set_goal:{goals[3][0]}"),
            ],
            [InlineKeyboardButton(text=t(lang, "keyboard.back"), callback_data="pref:back")],
        ]
    )


def pref_time_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=t(lang, "keyboard.time_fast"), callback_data="set_time:fast"),
                InlineKeyboardButton(text=t(lang, "keyboard.time_medium"), callback_data="set_time:medium"),
            ],
            [
                InlineKeyboardButton(text=t(lang, "keyboard.time_long"), callback_data="set_time:long"),
                InlineKeyboardButton(text=t(lang, "keyboard.time_any"), callback_data="set_time:any"),
            ],
            [InlineKeyboardButton(text=t(lang, "keyboard.back"), callback_data="pref:back")],
        ]
    )


def pref_lang_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=t("ru", "labels.language.ru"), callback_data="set_lang:ru"),
                InlineKeyboardButton(text=t("en", "labels.language.en"), callback_data="set_lang:en"),
            ],
            [InlineKeyboardButton(text=t(lang, "keyboard.back"), callback_data="pref:back")],
        ]
    )


def favorites_kb(recipes: list[tuple[str, str]], lang: str = "ru") -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text=f"⭐ {title}", callback_data=f"recipe:{rid}")]
        for rid, title in recipes
    ]
    if not buttons:
        buttons = [[InlineKeyboardButton(text=t(lang, "keyboard.back"), callback_data="back_main")]]
    else:
        buttons.append([InlineKeyboardButton(text=t(lang, "keyboard.back"), callback_data="back_main")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def premium_kb(is_premium: bool, lang: str = "ru") -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton(text=t(lang, "keyboard.premium_support"), url=DONATTY_URL)],
    ]
    if not is_premium:
        rows.append(
            [InlineKeyboardButton(text=t(lang, "keyboard.premium_check"), callback_data="premium:check")]
        )
    return InlineKeyboardMarkup(inline_keyboard=rows)
