from __future__ import annotations

from dataclasses import replace

from bot.i18n.en_recipes import EN_RECIPES
from bot.services.recipes import Recipe


def localize_recipe(recipe: Recipe, lang: str) -> Recipe:
    if lang != "en":
        return recipe
    tr = EN_RECIPES.get(recipe.id)
    if not tr:
        return recipe
    return replace(
        recipe,
        title=tr["title"],
        description=tr["description"],
        ingredients=tr["ingredients"],
        steps=tr["steps"],
        benefits=tr["benefits"],
        tips=tr["tips"],
    )


def localized_title(recipe: Recipe, lang: str) -> str:
    if lang == "en" and recipe.id in EN_RECIPES:
        return EN_RECIPES[recipe.id]["title"]
    return recipe.title
