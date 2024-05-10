from aiogram.fsm.state import StatesGroup, State


class QueryState(StatesGroup):
    story = State()
