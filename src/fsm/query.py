from aiogram.fsm.state import StatesGroup, State


class QueryState(StatesGroup):
    start = State()
    wait = State()
    story = State()
