from aiogram.fsm.state import StatesGroup, State


class QueryState(StatesGroup):
    wait = State()
    story = State()
