DONATTY_URL = "https://donatty.com/creator_bots"

PREMIUM_FEATURES = [
    "📆 Меню на неделю",
    "🍽 Эксклюзивные премиум-рецепты",
    "⭐ Безлимитное избранное",
    "🎯 Расширенные настройки питания",
]

# Выдан премиум по запросу автора
PREGRANTED_USERNAMES = {"fuckther47", "millka_2mky"}


def premium_status_text(is_premium: bool) -> str:
    features = "\n".join(f"  ✓ {f}" for f in PREMIUM_FEATURES)
    if is_premium:
        return (
            "<b>💎 Премиум активен</b>\n\n"
            "Спасибо, что поддерживаете проект! Вам доступно:\n"
            f"{features}\n\n"
            f"☕ Поддержать автора: <a href=\"{DONATTY_URL}\">Donatty</a>"
        )
    return (
        "<b>💎 Премиум</b>\n\n"
        "Откройте расширенные возможности бота:\n"
        f"{features}\n\n"
        "Поддержите автора — и получите премиум-доступ:\n"
        f"👉 <a href=\"{DONATTY_URL}\">Поддержать на Donatty</a>\n\n"
        "<i>После доната напишите /premium — доступ активируется автоматически "
        "для поддержавших (или свяжитесь с автором).</i>"
    )


def premium_required_text() -> str:
    return (
        "🔒 <b>Эта функция доступна в Премиум</b>\n\n"
        "📆 Меню на неделю и другие бонусы — для подписчиков премиум.\n\n"
        f"☕ Поддержать автора: <a href=\"{DONATTY_URL}\">Donatty</a>\n"
        "После поддержки нажмите /premium"
    )
