STRINGS = {
    "btn": {
        "find_recipe": "🍳 Find recipe",
        "random_recipe": "🎲 Random recipe",
        "menu_day": "📅 Daily menu",
        "menu_week": "📆 Weekly menu",
        "favorites": "⭐ Favorites",
        "settings": "⚙️ Settings",
        "premium": "💎 Premium",
        "support": "☕ Support author",
        "tips": "💡 Nutrition tips",
        "help": "❓ Help",
        "cancel": "❌ Cancel",
    },
    "labels": {
        "meal": {
            "breakfast": "🌅 Breakfast",
            "lunch": "☀️ Lunch",
            "dinner": "🌙 Dinner",
            "snack": "🍎 Snack",
            "dessert": "🍰 Dessert",
        },
        "diet": {
            "pp": "Healthy eating",
            "keto": "Keto",
            "low_carb": "Low carb",
            "vegan": "Vegan",
            "vegetarian": "Vegetarian",
            "gluten_free": "Gluten-free",
            "lactose_free": "Lactose-free",
        },
        "goal": {
            "weight_loss": "Weight loss",
            "muscle_gain": "Muscle gain",
            "maintain": "Maintenance",
            "detox": "Detox",
        },
        "time": {
            "fast": "⚡ Quick (≤20 min)",
            "medium": "🕐 Medium (21–40 min)",
            "long": "🕰 Long (>40 min)",
            "any": "Any time",
        },
        "difficulty": {
            "easy": "Easy",
            "medium": "Medium",
            "hard": "Hard",
        },
        "weekday": {
            "mon": "Mon",
            "tue": "Tue",
            "wed": "Wed",
            "thu": "Thu",
            "fri": "Fri",
            "sat": "Sat",
            "sun": "Sun",
        },
        "language": {
            "ru": "🇷🇺 Русский",
            "en": "🇬🇧 English",
        },
    },
    "welcome": {
        "text": (
            "Hi! 👋 I'm <b>Healthy Taste</b>, your healthy eating assistant.\n\n"
            "What shall we cook today? Tell me what's in your fridge, "
            "pick a meal type, or choose a category from the menu.\n\n"
            "🥗 I'll help you find tasty, healthy, balanced recipes!"
        ),
        "premium_active": "💎 <b>Premium active</b> — thank you for your support!",
        "support": "☕ Support the author: <a href=\"{url}\">Donatty</a>",
    },
    "help": {
        "text": (
            "<b>❓ Help — Healthy Taste</b>\n\n"
            "<b>Commands:</b>\n"
            "/start — welcome and main menu\n"
            "/random — random healthy recipe\n"
            "/menu — daily or weekly menu\n"
            "/preferences — your preferences\n"
            "/premium — premium and support\n"
            "/help — this help\n\n"
            "<b>Menu buttons:</b>\n"
            "🍳 <b>Find recipe</b> — by meal, diet, or ingredients\n"
            "🎲 <b>Random recipe</b> — based on your settings\n"
            "📅 <b>Daily menu</b> — balanced day plan\n"
            "📆 <b>Weekly menu</b> — 7-day plan\n"
            "⭐ <b>Favorites</b> — saved recipes\n"
            "⚙️ <b>Settings</b> — diet, goal, cook time, language\n"
            "💎 <b>Premium</b> — extra features\n"
            "☕ <b>Support author</b> — Donatty\n"
            "💡 <b>Nutrition tips</b> — useful advice\n\n"
            "Just type what's at home — e.g. «chicken, rice and vegetables» 🥕"
        ),
    },
    "tips": {
        "title": "<b>💡 Tip of the day</b>\n\n{tip}",
        "items": [
            (
                "💧 <b>Drink enough water</b>\n"
                "Aim for about 30–35 ml per kg of body weight. Water supports digestion, "
                "metabolism, and appetite control."
            ),
            (
                "🥦 <b>Half your plate — vegetables</b>\n"
                "Vegetables and greens should fill half the plate. "
                "They provide fiber, vitamins, and volume without extra calories."
            ),
            (
                "🍞 <b>Choose whole foods</b>\n"
                "Whole-grain bread, brown rice, oats — slow carbs "
                "keep you full longer and avoid sugar spikes."
            ),
            (
                "🥩 <b>Protein at every meal</b>\n"
                "20–30 g of protein per meal helps preserve muscle, "
                "boosts metabolism, and prolongs satiety."
            ),
            (
                "🥑 <b>Don't fear healthy fats</b>\n"
                "Avocado, nuts, olive oil, fish — sources of omega-3 "
                "and fat-soluble vitamins."
            ),
            (
                "⏰ <b>Regular eating schedule</b>\n"
                "Meals every 3–4 hours help stabilize energy "
                "and prevent overeating."
            ),
            (
                "🚫 <b>Less ultra-processed food</b>\n"
                "Avoid products with long lists of unfamiliar ingredients, "
                "trans fats, and hidden sugar."
            ),
            (
                "🍽 <b>Mindful eating</b>\n"
                "Eat slowly, without distractions. "
                "Your brain needs time to signal fullness."
            ),
        ],
    },
    "recipes": {
        "not_found": "Recipe not found.",
        "no_results": (
            "😔 No recipes found for this request.\n"
            "Try another category or change settings in ⚙️ Settings."
        ),
        "choose_category": "Choose a category or search method:",
        "choose_recipe": "Choose a recipe:",
        "choose_category_short": "Choose a category:",
        "fast_title": "⚡ Quick recipes (≤20 min)",
        "ingredients_prompt": (
            "🥕 Type what you have at home, separated by commas.\n"
            "Example: <i>chicken, rice, vegetables, avocado</i>"
        ),
        "search_cancelled": "Search cancelled.",
        "no_exact_match": "No exact match for «{query}», but here are similar recipes:",
        "found_count": "🥕 Found {count} recipes\nChoose one:",
        "favorites_empty": (
            "You have no favorite recipes yet.\n"
            "Tap ⭐ <b>Add to favorites</b> under any recipe!"
        ),
        "favorites_title": "<b>⭐ Favorite recipes ({count})</b>",
        "fav_added": "⭐ «{title}» added to favorites!",
        "fav_exists": "Already in favorites",
        "fav_removed": "Removed from favorites",
        "search_not_found": "No recipe found for «{query}».\n\n",
        "search_tip_1": "Try listing products separated by commas 🥕",
        "search_tip_2": "Or tap 🍳 <b>Find recipe</b> to pick a category",
        "search_tip_3": "Command /random — random recipe with your settings",
        "search_found": "🔍 Found {count} recipes for your query:",
    },
    "menu": {
        "choose_type": "📋 Choose menu type:",
        "building_week": "📋 Building weekly menu…",
        "daily_title": "<b>📅 Daily menu</b>\n",
        "weekly_title": "<b>📆 Weekly menu</b>\n",
        "recipe_missing": "  — recipe not found",
        "total_cal": "<b>Total: ~{cal} kcal</b>",
    },
    "prefs": {
        "title": "<b>⚙️ Your settings</b>\n\n",
        "diet_line": "🥗 <b>Diet:</b> {value}\n",
        "goal_line": "🎯 <b>Goal:</b> {value}\n",
        "time_line": "⏱ <b>Cook time:</b> {value}\n",
        "lang_line": "🌐 <b>Language:</b> {value}\n\n",
        "footer": "These settings are used for recipe matching and menus.",
        "choose_diet": "🥗 Choose diet type:",
        "choose_goal": "🎯 Choose your goal:",
        "choose_time": "⏱ Choose preferred cook time:",
        "choose_lang": "🌐 Choose language:",
        "lang_changed": "✅ Language changed to {lang}",
    },
    "premium": {
        "features": [
            "📆 Weekly menu",
            "🍽 Exclusive premium recipes",
            "⭐ Unlimited favorites",
            "🎯 Advanced nutrition settings",
        ],
        "active_title": "<b>💎 Premium active</b>\n\n",
        "active_body": "Thank you for supporting the project! You have access to:\n",
        "title": "<b>💎 Premium</b>\n\n",
        "body": "Unlock extended bot features:\n",
        "support_cta": "Support the author to get premium access:\n",
        "support_link": "👉 <a href=\"{url}\">Support on Donatty</a>\n\n",
        "support_footer": "☕ Support the author: <a href=\"{url}\">Donatty</a>",
        "note": (
            "<i>After donating, send /premium — access activates automatically "
            "for supporters (or contact the author).</i>"
        ),
        "required": (
            "🔒 <b>This feature requires Premium</b>\n\n"
            "📆 Weekly menu and other bonuses are for premium subscribers.\n\n"
            "☕ Support the author: <a href=\"{url}\">Donatty</a>\n"
            "After supporting, tap /premium"
        ),
    },
    "keyboard": {
        "placeholder": "Choose an action or type a query...",
        "back": "🔙 Back",
        "fav_add": "⭐ Add to favorites",
        "fav_remove": "💔 Remove from favorites",
        "another": "🎲 Another recipe",
        "back_categories": "🔙 Back to categories",
        "by_ingredients": "🥕 By ingredients",
        "fast_short": "⚡ Quick (≤20 min)",
        "menu_day_short": "📅 Daily",
        "menu_week_short": "📆 Weekly",
        "pref_diet": "🥗 Diet type",
        "pref_goal": "🎯 Goal",
        "pref_time": "⏱ Cook time",
        "pref_lang": "🌐 Language",
        "diet_pp": "Healthy",
        "diet_keto": "Keto",
        "diet_low_carb": "Low carb",
        "diet_vegan": "Vegan",
        "diet_veget": "Vegetarian",
        "diet_gluten": "Gluten-free",
        "diet_lactose": "Lactose-free",
        "time_fast": "⚡ Quick",
        "time_medium": "🕐 Medium",
        "time_long": "🕰 Long",
        "time_any": "Any",
        "premium_support": "☕ Support on Donatty",
        "premium_check": "🔄 Check status",
    },
    "format": {
        "time": "⏱ <b>Time:</b> {min} min",
        "servings": "🍽 <b>Servings:</b> {n}",
        "difficulty": "📊 <b>Difficulty:</b> {value}",
        "type": "🏷 <b>Type:</b> {value}",
        "ingredients": "<b>🛒 Ingredients:</b>",
        "steps": "<b>👨‍🍳 Instructions:</b>",
        "nutrition": "<b>📈 Nutrition (per serving):</b>",
        "calories": "  🔥 {cal} kcal",
        "protein": "  🥩 Protein: {g} g",
        "fat": "  🧈 Fat: {g} g",
        "carbs": "  🍞 Carbs: {g} g",
        "benefits": "<b>💚 Health benefits:</b>",
        "tips": "<b>🔄 Variations & tips:</b>",
        "short_time": "⏱ {min} min",
        "short_cal": "🔥 {cal} kcal",
    },
}
