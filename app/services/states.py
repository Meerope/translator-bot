from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    text = State()
    code_to = State()
    code_from = State()