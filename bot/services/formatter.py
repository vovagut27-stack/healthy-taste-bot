from bot.i18n import (
    get_difficulty_labels,
    get_meal_labels,
    localize_recipe,
    localized_title,
    t,
)
from bot.services.recipes import Recipe


def format_recipe(recipe: Recipe, *, is_favorite: bool = False, lang: str = "ru") -> str:
    recipe = localize_recipe(recipe, lang)
    meal_labels = get_meal_labels(lang)
    difficulty_labels = get_difficulty_labels(lang)
    fav_mark = " ⭐" if is_favorite else ""
    ingredients = "\n".join(f"  • {item}" for item in recipe.ingredients)
    steps = "\n".join(f"  {i}. {step}" for i, step in enumerate(recipe.steps, 1))
    benefits = "\n".join(f"  ✓ {b}" for b in recipe.benefits)
    tips = "\n".join(f"  💡 {tip}" for tip in recipe.tips)

    return (
        f"<b>{recipe.emoji} {recipe.title}</b>{fav_mark}\n"
        f"<i>{recipe.description}</i>\n\n"
        f"{t(lang, 'format.time', min=recipe.cook_time_min)} | "
        f"{t(lang, 'format.servings', n=recipe.servings)} | "
        f"{t(lang, 'format.difficulty', value=difficulty_labels[recipe.difficulty])}\n"
        f"{t(lang, 'format.type', value=meal_labels[recipe.meal_type])}\n\n"
        f"{t(lang, 'format.ingredients')}\n{ingredients}\n\n"
        f"{t(lang, 'format.steps')}\n{steps}\n\n"
        f"{t(lang, 'format.nutrition')}\n"
        f"{t(lang, 'format.calories', cal=recipe.calories)}\n"
        f"{t(lang, 'format.protein', g=recipe.protein)}\n"
        f"{t(lang, 'format.fat', g=recipe.fat)}\n"
        f"{t(lang, 'format.carbs', g=recipe.carbs)}\n\n"
        f"{t(lang, 'format.benefits')}\n{benefits}\n\n"
        f"{t(lang, 'format.tips')}\n{tips}"
    )


def format_recipe_short(recipe: Recipe, lang: str = "ru") -> str:
    recipe = localize_recipe(recipe, lang)
    meal_labels = get_meal_labels(lang)
    return (
        f"{recipe.emoji} <b>{recipe.title}</b>\n"
        f"{t(lang, 'format.short_time', min=recipe.cook_time_min)} | "
        f"{t(lang, 'format.short_cal', cal=recipe.calories)} | "
        f"{meal_labels[recipe.meal_type]}"
    )


def format_daily_menu(menu: dict[str, Recipe | None], lang: str = "ru") -> str:
    meal_labels = get_meal_labels(lang)
    lines = [t(lang, "menu.daily_title")]
    total_cal = 0
    for meal_key, label in meal_labels.items():
        if meal_key not in menu:
            continue
        recipe = menu[meal_key]
        if recipe:
            lines.append(f"\n{label}\n{format_recipe_short(recipe, lang)}")
            total_cal += recipe.calories
        else:
            lines.append(f"\n{label}\n{t(lang, 'menu.recipe_missing')}")
    lines.append(f"\n\n{t(lang, 'menu.total_cal', cal=total_cal)}")
    return "\n".join(lines)


def format_weekly_menu(week: list[dict], lang: str = "ru") -> str:
    from bot.i18n import get_weekday_labels

    days = get_weekday_labels(lang)
    meal_labels = get_meal_labels(lang)
    lines = [t(lang, "menu.weekly_title")]
    for i, day_menu in enumerate(week):
        lines.append(f"\n<b>{days[i]}</b>")
        for meal_key in ["breakfast", "lunch", "dinner"]:
            recipe = day_menu.get(meal_key)
            if recipe:
                title = localized_title(recipe, lang)
                lines.append(f"  {meal_labels[meal_key]}: {recipe.emoji} {title}")
    return "\n".join(lines)
