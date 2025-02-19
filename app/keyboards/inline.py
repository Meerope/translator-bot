from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.data.languages import languages


async def get_keyboard_langs(btn_type: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    for code, language in languages.items():
        button = InlineKeyboardButton(
            text=language,
            callback_data=f'{btn_type}:{code}',
        )
        keyboard.add(button)
    keyboard.adjust(1)

    return keyboard.as_markup()
