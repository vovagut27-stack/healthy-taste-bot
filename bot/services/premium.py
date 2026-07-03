from bot.i18n import get_list, t

DONATTY_URL = "https://donatty.com/creator_bots"

PREGRANTED_USERNAMES = {"fuckther47", "millka_2mky"}


def premium_status_text(is_premium: bool, lang: str = "ru") -> str:
    features = "\n".join(f"  ✓ {f}" for f in get_list(lang, "premium.features"))
    if is_premium:
        return (
            t(lang, "premium.active_title")
            + t(lang, "premium.active_body")
            + f"{features}\n\n"
            + t(lang, "premium.support_footer", url=DONATTY_URL)
        )
    return (
        t(lang, "premium.title")
        + t(lang, "premium.body")
        + f"{features}\n\n"
        + t(lang, "premium.support_cta")
        + t(lang, "premium.support_link", url=DONATTY_URL)
        + t(lang, "premium.note")
    )


def premium_required_text(lang: str = "ru") -> str:
    return t(lang, "premium.required", url=DONATTY_URL)
