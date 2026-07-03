from __future__ import annotations

from bot.i18n.core import t


def get_meal_labels(lang: str) -> dict[str, str]:
    return {
        "breakfast": t(lang, "labels.meal.breakfast"),
        "lunch": t(lang, "labels.meal.lunch"),
        "dinner": t(lang, "labels.meal.dinner"),
        "snack": t(lang, "labels.meal.snack"),
        "dessert": t(lang, "labels.meal.dessert"),
    }


def get_diet_labels(lang: str) -> dict[str, str]:
    return {
        "pp": t(lang, "labels.diet.pp"),
        "keto": t(lang, "labels.diet.keto"),
        "low_carb": t(lang, "labels.diet.low_carb"),
        "vegan": t(lang, "labels.diet.vegan"),
        "vegetarian": t(lang, "labels.diet.vegetarian"),
        "gluten_free": t(lang, "labels.diet.gluten_free"),
        "lactose_free": t(lang, "labels.diet.lactose_free"),
    }


def get_goal_labels(lang: str) -> dict[str, str]:
    return {
        "weight_loss": t(lang, "labels.goal.weight_loss"),
        "muscle_gain": t(lang, "labels.goal.muscle_gain"),
        "maintain": t(lang, "labels.goal.maintain"),
        "detox": t(lang, "labels.goal.detox"),
    }


def get_time_labels(lang: str) -> dict[str, str]:
    return {
        "fast": t(lang, "labels.time.fast"),
        "medium": t(lang, "labels.time.medium"),
        "long": t(lang, "labels.time.long"),
        "any": t(lang, "labels.time.any"),
    }


def get_difficulty_labels(lang: str) -> dict[str, str]:
    return {
        "easy": t(lang, "labels.difficulty.easy"),
        "medium": t(lang, "labels.difficulty.medium"),
        "hard": t(lang, "labels.difficulty.hard"),
    }


def get_weekday_labels(lang: str) -> list[str]:
    return [
        t(lang, "labels.weekday.mon"),
        t(lang, "labels.weekday.tue"),
        t(lang, "labels.weekday.wed"),
        t(lang, "labels.weekday.thu"),
        t(lang, "labels.weekday.fri"),
        t(lang, "labels.weekday.sat"),
        t(lang, "labels.weekday.sun"),
    ]
