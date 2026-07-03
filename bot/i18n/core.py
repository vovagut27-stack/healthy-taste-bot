from __future__ import annotations

from typing import Any

from bot.i18n import en, ru

SUPPORTED_LANGS = frozenset({"ru", "en"})
DEFAULT_LANG = "ru"

LOCALES: dict[str, dict[str, Any]] = {
    "ru": ru.STRINGS,
    "en": en.STRINGS,
}


def _resolve(lang: str, key: str) -> Any:
    lang = lang if lang in LOCALES else DEFAULT_LANG
    node: Any = LOCALES[lang]
    for part in key.split("."):
        node = node[part]
    return node


def t(lang: str, key: str, **kwargs: Any) -> str:
    value = _resolve(lang, key)
    if not isinstance(value, str):
        raise KeyError(f"Translation key is not a string: {key}")
    return value.format(**kwargs) if kwargs else value


def btn(lang: str, key: str) -> str:
    return t(lang, f"btn.{key}")


def all_btn(key: str) -> frozenset[str]:
    return frozenset(t(lang, f"btn.{key}") for lang in LOCALES)


def is_btn(text: str | None, key: str) -> bool:
    return bool(text and text in all_btn(key))


def all_menu_buttons() -> frozenset[str]:
    keys = (
        "find_recipe",
        "random_recipe",
        "menu_day",
        "menu_week",
        "favorites",
        "settings",
        "premium",
        "support",
        "tips",
        "help",
        "cancel",
    )
    return frozenset().union(*(all_btn(k) for k in keys))


def is_cancel(text: str | None) -> bool:
    return is_btn(text, "cancel")


def get_list(lang: str, key: str) -> list[Any]:
    value = _resolve(lang, key)
    if not isinstance(value, list):
        raise KeyError(f"Translation key is not a list: {key}")
    return value
