from dataclasses import dataclass, field


@dataclass
class Recipe:
    id: str
    title: str
    emoji: str
    description: str
    meal_type: str  # breakfast, lunch, dinner, snack, dessert
    diet_tags: list[str]
    goal_tags: list[str]
    cook_time_min: int
    difficulty: str  # easy, medium, hard
    servings: int
    ingredients: list[str]
    steps: list[str]
    calories: int
    protein: float
    fat: float
    carbs: float
    benefits: list[str]
    tips: list[str]
    ingredient_keywords: list[str] = field(default_factory=list)


RECIPES: list[Recipe] = [
    Recipe(
        id="oat_bowl",
        title="Овсяная боул с ягодами и орехами",
        emoji="🥣",
        description="Сытный завтрак с клетчаткой и антиоксидантами — идеальный старт дня!",
        meal_type="breakfast",
        diet_tags=["pp", "vegetarian", "gluten_free", "lactose_free"],
        goal_tags=["maintain", "weight_loss"],
        cook_time_min=10,
        difficulty="easy",
        servings=1,
        ingredients=[
            "Овсяные хлопья — 50 г",
            "Молоко растительное (миндальное/овсяное) — 150 мл",
            "Свежие или замороженные ягоды — 80 г",
            "Грецкие орехи — 15 г",
            "Мёд — 1 ч. л.",
            "Корица — щепотка",
        ],
        steps=[
            "Залейте овсянку тёплым растительным молоком и дайте настояться 5 минут.",
            "Добавьте ягоды, измельчённые орехи и мёд.",
            "Посыпьте корицей и подавайте сразу.",
        ],
        calories=320,
        protein=10,
        fat=12,
        carbs=42,
        benefits=[
            "Много клетчатки для пищеварения",
            "Медленные углеводы — долгое насыщение",
            "Антиоксиданты из ягод",
        ],
        tips=[
            "Замените мёд на стевию для ещё меньшей калорийности",
            "Добавьте ложку арахисовой пасты для белка",
        ],
        ingredient_keywords=["овсянка", "овсяные", "ягоды", "орехи", "молоко"],
    ),
    Recipe(
        id="avocado_toast",
        title="Тост с авокадо и яйцом пашот",
        emoji="🥑",
        description="Классика ПП-завтрака: полезные жиры, белок и хрустящий хлеб.",
        meal_type="breakfast",
        diet_tags=["pp", "vegetarian"],
        goal_tags=["maintain", "muscle_gain"],
        cook_time_min=15,
        difficulty="medium",
        servings=1,
        ingredients=[
            "Цельнозерновой хлеб — 1 ломтик",
            "Авокадо — ½ шт.",
            "Яйцо — 1 шт.",
            "Лимонный сок — 1 ч. л.",
            "Соль, перец — по вкусу",
            "Микрозелень — для подачи",
        ],
        steps=[
            "Поджарьте хлеб в тостере до золотистой корочки.",
            "Разомните авокадо с лимонным соком, солью и перцем.",
            "Сварите яйцо пашот: 3 минуты в кипящей воде с уксусом.",
            "Намажьте хлеб авокадо, сверху положите яйцо и микрозелень.",
        ],
        calories=380,
        protein=16,
        fat=22,
        carbs=28,
        benefits=[
            "Мононенасыщенные жиры для сердца",
            "Полноценный белок из яйца",
            "Клетчатка из цельнозернового хлеба",
        ],
        tips=[
            "Без глютена: используйте безглютеновый хлеб",
            "Для веганов: замените яйцо на тофу-скрамбл",
        ],
        ingredient_keywords=["авокадо", "яйцо", "хлеб", "тост"],
    ),
    Recipe(
        id="chicken_salad",
        title="Салат с куриной грудкой и киноа",
        emoji="🥗",
        description="Сбалансированный обед: белок, сложные углеводы и свежие овощи.",
        meal_type="lunch",
        diet_tags=["pp", "gluten_free", "lactose_free"],
        goal_tags=["weight_loss", "muscle_gain", "maintain"],
        cook_time_min=25,
        difficulty="easy",
        servings=2,
        ingredients=[
            "Куриная грудка — 300 г",
            "Киноа — 80 г (сухая)",
            "Огурец — 1 шт.",
            "Помидор — 1 шт.",
            "Шпинат — 50 г",
            "Оливковое масло — 1 ст. л.",
            "Лимонный сок — 2 ст. л.",
            "Соль, перец, чеснок — по вкусу",
        ],
        steps=[
            "Отварите киноа по инструкции на упаковке (около 15 мин).",
            "Куриную грудку посолите, обжарьте на сухой сковороде 6–7 мин с каждой стороны.",
            "Нарежьте овощи, смешайте с киноа и шпинатом.",
            "Нарежьте курицу, добавьте в салат.",
            "Заправьте оливковым маслом, лимоном и специями.",
        ],
        calories=420,
        protein=38,
        fat=14,
        carbs=32,
        benefits=[
            "Высокое содержание белка",
            "Полный набор аминокислот из киноа",
            "Низкая калорийность при высокой сытности",
        ],
        tips=[
            "Замените курицу на индейку или тофу",
            "Добавьте авокадо для полезных жиров",
        ],
        ingredient_keywords=["курица", "куриная", "киноа", "салат", "огурец", "помидор"],
    ),
    Recipe(
        id="veggie_soup",
        title="Овощной суп-пюре с тыквой",
        emoji="🍲",
        description="Лёгкий и согревающий суп — идеален для ужина или детокса.",
        meal_type="dinner",
        diet_tags=["pp", "vegan", "vegetarian", "gluten_free", "lactose_free"],
        goal_tags=["weight_loss", "detox", "maintain"],
        cook_time_min=30,
        difficulty="easy",
        servings=4,
        ingredients=[
            "Тыква — 400 г",
            "Морковь — 1 шт.",
            "Лук — 1 шт.",
            "Картофель — 1 шт. (небольшой)",
            "Чеснок — 2 зубчика",
            "Оливковое масло — 1 ст. л.",
            "Вода или овощной бульон — 800 мл",
            "Соль, перец, имбирь — по вкусу",
        ],
        steps=[
            "Нарежьте овощи кубиками.",
            "Обжарьте лук и чеснок на оливковом масле 2 минуты.",
            "Добавьте остальные овощи, залейте бульоном, варите 20 минут.",
            "Измельчите блендером до однородности.",
            "Приправьте имбирём, солью и перцем.",
        ],
        calories=180,
        protein=4,
        fat=5,
        carbs=28,
        benefits=[
            "Богат бета-каротином из тыквы",
            "Лёгкий для пищеварения",
            "Низкая калорийность",
        ],
        tips=[
            "Добавьте кокосовое молоко для кремовой текстуры",
            "Подавайте с семенами тыквы",
        ],
        ingredient_keywords=["тыква", "морковь", "лук", "суп", "овощи"],
    ),
    Recipe(
        id="salmon_bowl",
        title="Боул с лососем и бурым рисом",
        emoji="🐟",
        description="Омега-3, сложные углеводы и яркие овощи — идеальный ужин.",
        meal_type="dinner",
        diet_tags=["pp", "gluten_free", "lactose_free"],
        goal_tags=["muscle_gain", "maintain"],
        cook_time_min=35,
        difficulty="medium",
        servings=2,
        ingredients=[
            "Филе лосося — 300 г",
            "Бурый рис — 120 г (сухой)",
            "Авокадо — 1 шт.",
            "Огурец — 1 шт.",
            "Эдамame — 100 г",
            "Соевый соус (низкосолёный) — 2 ст. л.",
            "Кунжут — 1 ч. л.",
            "Лимон — ½ шт.",
        ],
        steps=[
            "Отварите бурый рис (около 30 мин).",
            "Лосось посолите, запеките при 180°C 15 минут.",
            "Нарежьте авокадо и огурец.",
            "Разложите рис, лосось, овощи и эдамame в миски.",
            "Полейте соевым соусом, посыпьте кунжутом, добавьте лимон.",
        ],
        calories=520,
        protein=35,
        fat=22,
        carbs=45,
        benefits=[
            "Омега-3 жирные кислоты для мозга и сердца",
            "Качественный белок",
            "Медленные углеводы",
        ],
        tips=[
            "Замените лосось на форель или тофу",
            "Добавьте водоросли нори для йода",
        ],
        ingredient_keywords=["лосось", "рыба", "рис", "авокадо", "эдамame"],
    ),
    Recipe(
        id="greek_yogurt_snack",
        title="Греческий йогурт с фруктами и семенами",
        emoji="🍓",
        description="Быстрый перекус с белком и пробиотиками.",
        meal_type="snack",
        diet_tags=["pp", "vegetarian", "gluten_free"],
        goal_tags=["weight_loss", "maintain", "muscle_gain"],
        cook_time_min=5,
        difficulty="easy",
        servings=1,
        ingredients=[
            "Греческий йогурт 2% — 150 г",
            "Банан — ½ шт.",
            "Клубника — 50 г",
            "Семена чиа — 1 ч. л.",
            "Мёд — 1 ч. л.",
        ],
        steps=[
            "Выложите йогurt в миску.",
            "Нарежьте банан и клубнику, добавьте сверху.",
            "Посыпьте семенами чиа и полейте мёдом.",
        ],
        calories=220,
        protein=15,
        fat=5,
        carbs=30,
        benefits=[
            "Пробиотики для микрофлоры кишечника",
            "Быстрый источник белка",
            "Омега-3 из семян чиа",
        ],
        tips=[
            "Без лактозы: используйте кокосовый йогурт",
            "Замените мёд на ягодное пюре",
        ],
        ingredient_keywords=["йогурт", "банан", "клубника", "фрукты"],
    ),
    Recipe(
        id="energy_balls",
        title="Энергетические шарики без выпечки",
        emoji="🍫",
        description="Полезный десерт без сахара — идеален для перекуса.",
        meal_type="dessert",
        diet_tags=["pp", "vegan", "vegetarian", "gluten_free", "lactose_free"],
        goal_tags=["maintain", "muscle_gain"],
        cook_time_min=15,
        difficulty="easy",
        servings=8,
        ingredients=[
            "Финики без косточек — 150 г",
            "Миндаль — 80 г",
            "Какао-порошок — 2 ст. л.",
            "Кокосовая стружка — 3 ст. л.",
            "Ваниль — щепотка",
            "Щепотка соли",
        ],
        steps=[
            "Замочите финики в тёплой воде на 10 минут.",
            "Измельчите миндаль в блендере до муки.",
            "Добавьте финики, какао, ваниль и соль, пробейте до однородности.",
            "Сформируйте шарики, обваляйте в кокосовой стружке.",
            "Уберите в холодильник на 30 минут.",
        ],
        calories=95,
        protein=2,
        fat=5,
        carbs=12,
        benefits=[
            "Натуральная сладость без рафинированного сахара",
            "Полезные жиры из орехов",
            "Быстрый перекус перед тренировкой",
        ],
        tips=[
            "Добавьте протеиновый порошок для большего белка",
            "Храните в холодильнике до 7 дней",
        ],
        ingredient_keywords=["финики", "миндаль", "какао", "орехи", "десерт"],
    ),
    Recipe(
        id="keto_omelette",
        title="Кето-омлет с шпинатом и сыром",
        emoji="🍳",
        description="Низкоуглеводный завтрак с высоким содержанием белка и жиров.",
        meal_type="breakfast",
        diet_tags=["keto", "low_carb", "vegetarian", "gluten_free"],
        goal_tags=["weight_loss", "maintain"],
        cook_time_min=12,
        difficulty="easy",
        servings=1,
        ingredients=[
            "Яйца — 3 шт.",
            "Шпинат — 50 г",
            "Сыр моцарелла — 30 г",
            "Сливочное масло — 10 г",
            "Соль, перец — по вкусу",
        ],
        steps=[
            "Обжарьте шпинат на сливочном масле 1–2 минуты.",
            "Взбейте яйца с солью и перцем.",
            "Вылейте на сковороду, добавьте сыр.",
            "Готовьте на среднем огне 4–5 минут, сложите пополам.",
        ],
        calories=380,
        protein=26,
        fat=28,
        carbs=4,
        benefits=[
            "Минимум углеводов — подходит для кето",
            "Высокое содержание белка",
            "Железо и фолиевая кислота из шпината",
        ],
        tips=[
            "Добавьте грибы или авокадо",
            "Без лактозы: используйте vegan-сир",
        ],
        ingredient_keywords=["яйца", "омлет", "шпинат", "сыр"],
    ),
    Recipe(
        id="lentil_curry",
        title="Чечевичное карри с овощами",
        emoji="🌿",
        description="Сытное веганское блюдо с растительным белком и специями.",
        meal_type="lunch",
        diet_tags=["vegan", "vegetarian", "pp", "gluten_free", "lactose_free"],
        goal_tags=["weight_loss", "maintain", "detox"],
        cook_time_min=35,
        difficulty="medium",
        servings=4,
        ingredients=[
            "Красная чечевица — 200 г",
            "Кокосовое молоко — 200 мл",
            "Помидоры — 2 шт.",
            "Лук — 1 шт.",
            "Морковь — 1 шт.",
            "Куркума — 1 ч. л.",
            "Имбирь — 1 ч. л. (тёртый)",
            "Чеснок — 2 зубчика",
            "Оливковое масло — 1 ст. л.",
        ],
        steps=[
            "Обжарьте лук, чеснок и имбирь на масле.",
            "Добавьте нарезанные овощи и куркуму, готовьте 3 минуты.",
            "Залейте чечевицу водой (500 мл), добавьте помидоры.",
            "Варите 20 минут, в конце добавьте кокосовое молоко.",
            "Приправьте солью и подавайте с рисом или без.",
        ],
        calories=290,
        protein=14,
        fat=10,
        carbs=38,
        benefits=[
            "Растительный белок и железо",
            "Противовоспалительные свойства куркумы",
            "Высокое содержание клетчатки",
        ],
        tips=[
            "Добавьте шпинат в конце приготовления",
            "Подавайте с коричневым рисом для полноценного обеда",
        ],
        ingredient_keywords=["чечевица", "карри", "овощи", "кокосовое молоко"],
    ),
    Recipe(
        id="zucchini_pasta",
        title="Паста из кабачков с томатным соусом",
        emoji="🍝",
        description="Низкоуглеводная альтернатива пасте — лёгкий и быстрый ужин.",
        meal_type="dinner",
        diet_tags=["pp", "low_carb", "vegetarian", "gluten_free", "lactose_free"],
        goal_tags=["weight_loss", "maintain"],
        cook_time_min=20,
        difficulty="easy",
        servings=2,
        ingredients=[
            "Кабачки — 2 шт. (средних)",
            "Помидоры — 3 шт.",
            "Чеснок — 2 зубчика",
            "Базилик — горсть",
            "Оливковое масло — 2 ст. л.",
            "Пармезан — 20 г (опционально)",
            "Соль, перец — по вкусу",
        ],
        steps=[
            "С помощью спiralizer или овощечистки нарежьте кабачки «спagetti».",
            "Обжарьте чеснок на оливковом масле, добавьте нарезанные помидоры.",
            "Тушите соус 10 минут, добавьте базилик.",
            "Обжарьте кабачковую пасту 2–3 минуты, смешайте с соусом.",
            "Подавайте с пармезаном.",
        ],
        calories=210,
        protein=8,
        fat=12,
        carbs=18,
        benefits=[
            "Минимум калорий при большом объёме",
            "Витамины A и C из кабачков",
            "Без глютена",
        ],
        tips=[
            "Не переваривайте кабачки — они станут водянистыми",
            "Добавьте куриную грудку или креветки для белка",
        ],
        ingredient_keywords=["кабачок", "кабачки", "помидор", "паста", "томат"],
    ),
    Recipe(
        id="smoothie_bowl",
        title="Смузи-боул с манго и гранолой",
        emoji="🥭",
        description="Освежающий завтрак или перекус — красиво и полезно!",
        meal_type="breakfast",
        diet_tags=["pp", "vegetarian", "gluten_free"],
        goal_tags=["maintain", "detox"],
        cook_time_min=10,
        difficulty="easy",
        servings=1,
        ingredients=[
            "Замороженное манго — 150 г",
            "Банан — 1 шт.",
            "Растительное молоко — 80 мл",
            "Гранола — 30 г",
            "Кокосовая стружка — 1 ст. л.",
            "Семена чиа — 1 ч. л.",
        ],
        steps=[
            "Пробейте манго, банан и молоко в блендере до густой консистенции.",
            "Выложите в миску, сверху — гранолу, кокос и семена чиа.",
            "Добавьте свежие ягоды по желанию.",
        ],
        calories=340,
        protein=8,
        fat=10,
        carbs=55,
        benefits=[
            "Витамин C и бета-каротин",
            "Клетчатка из гранолы",
            "Натуральная энергия без сахара",
        ],
        tips=[
            "Используйте замороженные ягоды вместо манго",
            "Добавьте протеин для послетренировочного перекуса",
        ],
        ingredient_keywords=["манго", "банан", "смузи", "гранола"],
    ),
    Recipe(
        id="turkey_wrap",
        title="Ролл с индейкой и овощами",
        emoji="🌯",
        description="Быстрый обед на ходу — белок, клетчатка и минимум калорий.",
        meal_type="lunch",
        diet_tags=["pp", "low_carb", "lactose_free"],
        goal_tags=["weight_loss", "muscle_gain"],
        cook_time_min=15,
        difficulty="easy",
        servings=1,
        ingredients=[
            "Лаваш цельнозерновой — 1 шт.",
            "Филе индейки — 100 г",
            "Авокадо — ½ шт.",
            "Огурец — ½ шт.",
            "Листья салата — 30 г",
            "Горчица — 1 ч. л.",
            "Соль, перец — по вкусу",
        ],
        steps=[
            "Подогрейте лаваш, намажьте горчицей.",
            "Выложите салат, нарезанные овощи и авокадо.",
            "Добавьте нарезанную индейку, посолите.",
            "Плотно сверните ролл, разрежьте пополам.",
        ],
        calories=350,
        protein=28,
        fat=14,
        carbs=30,
        benefits=[
            "Постный белок из индейки",
            "Удобно брать с собой",
            "Сбалансированный макросостав",
        ],
        tips=[
            "Замените лавash на листья салата для кето-версии",
            "Добавьте хумус для разнообразия",
        ],
        ingredient_keywords=["индейка", "лаваш", "авокадо", "рулон", "wrap"],
    ),
]

MEAL_LABELS = {
    "breakfast": "🌅 Завтрак",
    "lunch": "☀️ Обед",
    "dinner": "🌙 Ужин",
    "snack": "🍎 Перекус",
    "dessert": "🍰 Десерт",
}

DIET_LABELS = {
    "pp": "ПП (правильное питание)",
    "keto": "Кето",
    "low_carb": "Низкоуглеводное",
    "vegan": "Веган",
    "vegetarian": "Вегетарианское",
    "gluten_free": "Без глютена",
    "lactose_free": "Без лактозы",
}

GOAL_LABELS = {
    "weight_loss": "Похудение",
    "muscle_gain": "Набор массы",
    "maintain": "Поддержание формы",
    "detox": "Детокс",
}

TIME_LABELS = {
    "fast": "⚡ Быстро (≤20 мин)",
    "medium": "🕐 Средне (21–40 мин)",
    "long": "🕰 Долго (>40 мин)",
    "any": "Любое время",
}

DIFFICULTY_LABELS = {
    "easy": "Легко",
    "medium": "Средне",
    "hard": "Сложно",
}


def get_recipe_by_id(recipe_id: str) -> Recipe | None:
    for recipe in RECIPES:
        if recipe.id == recipe_id:
            return recipe
    return None


def filter_recipes(
    *,
    meal_type: str | None = None,
    diet: str | None = None,
    goal: str | None = None,
    max_time: str | None = None,
    ingredients: list[str] | None = None,
) -> list[Recipe]:
    result = list(RECIPES)

    if meal_type:
        result = [r for r in result if r.meal_type == meal_type]

    if diet and diet != "any":
        result = [r for r in result if diet in r.diet_tags]

    if goal and goal != "any":
        result = [r for r in result if goal in r.goal_tags]

    if max_time == "fast":
        result = [r for r in result if r.cook_time_min <= 20]
    elif max_time == "medium":
        result = [r for r in result if 21 <= r.cook_time_min <= 40]
    elif max_time == "long":
        result = [r for r in result if r.cook_time_min > 40]

    if ingredients:
        normalized = [i.lower().strip() for i in ingredients if i.strip()]
        if normalized:
            matched = []
            for recipe in result:
                keywords = recipe.ingredient_keywords + [
                    part.lower()
                    for ing in recipe.ingredients
                    for part in ing.split("—")[0].split(",")
                ]
                if any(
                    any(kw in ing or ing in kw for kw in keywords)
                    for ing in normalized
                ):
                    matched.append(recipe)
            result = matched if matched else result

    return result


def get_random_recipe(**filters) -> Recipe | None:
    import random

    filtered = filter_recipes(**filters)
    return random.choice(filtered) if filtered else None


def build_daily_menu(diet: str = "pp", goal: str = "maintain") -> dict[str, Recipe | None]:
    import random

    meals = ["breakfast", "lunch", "dinner", "snack"]
    menu: dict[str, Recipe | None] = {}
    used_ids: set[str] = set()

    for meal in meals:
        candidates = filter_recipes(meal_type=meal, diet=diet, goal=goal)
        candidates = [r for r in candidates if r.id not in used_ids]
        if candidates:
            recipe = random.choice(candidates)
            menu[meal] = recipe
            used_ids.add(recipe.id)
        else:
            fallback = filter_recipes(meal_type=meal)
            fallback = [r for r in fallback if r.id not in used_ids]
            menu[meal] = random.choice(fallback) if fallback else None

    return menu


def build_weekly_menu(diet: str = "pp", goal: str = "maintain") -> list[dict[str, Recipe | None]]:
    import random

    days = []
    for _ in range(7):
        day_menu = build_daily_menu(diet=diet, goal=goal)
        days.append(day_menu)
    return days
