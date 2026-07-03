from aiogram.fsm.state import State, StatesGroup


class IngredientSearch(StatesGroup):
    waiting_for_ingredients = State()


class PreferencesSetup(StatesGroup):
    choosing_diet = State()
    choosing_goal = State()
    choosing_time = State()
