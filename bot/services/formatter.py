from bot.services.recipes import (
    DIFFICULTY_LABELS,
    MEAL_LABELS,
    Recipe,
)


def format_recipe(recipe: Recipe, *, is_favorite: bool = False) -> str:
    fav_mark = " ⭐" if is_favorite else ""
    ingredients = "\n".join(f"  • {item}" for item in recipe.ingredients)
    steps = "\n".join(f"  {i}. {step}" for i, step in enumerate(recipe.steps, 1))
    benefits = "\n".join(f"  ✓ {b}" for b in recipe.benefits)
    tips = "\n".join(f"  💡 {t}" for t in recipe.tips)

    return (
        f"<b>{recipe.emoji} {recipe.title}</b>{fav_mark}\n"
        f"<i>{recipe.description}</i>\n\n"
        f"⏱ <b>Время:</b> {recipe.cook_time_min} мин | "
        f"🍽 <b>Порций:</b> {recipe.servings} | "
        f"📊 <b>Сложность:</b> {DIFFICULTY_LABELS[recipe.difficulty]}\n"
        f"🏷 <b>Тип:</b> {MEAL_LABELS[recipe.meal_type]}\n\n"
        f"<b>🛒 Ингредиенты:</b>\n{ingredients}\n\n"
        f"<b>👨‍🍳 Приготовление:</b>\n{steps}\n\n"
        f"<b>📈 Пищевая ценность (на 1 порцию):</b>\n"
        f"  🔥 {recipe.calories} ккал\n"
        f"  🥩 Белки: {recipe.protein} г\n"
        f"  🧈 Жиры: {recipe.fat} г\n"
        f"  🍞 Углеводы: {recipe.carbs} г\n\n"
        f"<b>💚 Полезные свойства:</b>\n{benefits}\n\n"
        f"<b>🔄 Вариации и советы:</b>\n{tips}"
    )


def format_recipe_short(recipe: Recipe) -> str:
    return (
        f"{recipe.emoji} <b>{recipe.title}</b>\n"
        f"⏱ {recipe.cook_time_min} мин | 🔥 {recipe.calories} ккал | "
        f"{MEAL_LABELS[recipe.meal_type]}"
    )


def format_daily_menu(menu: dict[str, "Recipe | None"]) -> str:
    from bot.services.recipes import MEAL_LABELS

    lines = ["<b>📅 Меню на день</b>\n"]
    total_cal = 0
    for meal_key, label in MEAL_LABELS.items():
        if meal_key not in menu:
            continue
        recipe = menu[meal_key]
        if recipe:
            lines.append(
                f"\n{label}\n{format_recipe_short(recipe)}"
            )
            total_cal += recipe.calories
        else:
            lines.append(f"\n{label}\n  — рецепт не найден")
    lines.append(f"\n\n<b>Итого: ~{total_cal} ккал</b>")
    return "\n".join(lines)


def format_weekly_menu(week: list[dict]) -> str:
    days_ru = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    lines = ["<b>📆 Меню на неделю</b>\n"]
    for i, day_menu in enumerate(week):
        lines.append(f"\n<b>{days_ru[i]}</b>")
        for meal_key in ["breakfast", "lunch", "dinner"]:
            recipe = day_menu.get(meal_key)
            if recipe:
                lines.append(f"  {MEAL_LABELS[meal_key]}: {recipe.emoji} {recipe.title}")
    return "\n".join(lines)
