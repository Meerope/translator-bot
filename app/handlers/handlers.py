import app.services.translation as tr
import app.keyboards.inline as inline

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from app.services.states import Form

router = Router()


@router.message(CommandStart())
async def cmd_start(msg: Message):
    await msg.answer('Привет! Это бот для перевода.\n\nОтправьте сообщение')


@router.message(F.text)
async def get_from_lang(msg: Message, state: FSMContext):
    await state.set_state(Form.text)
    await state.update_data(text=msg.text)

    keyboard_langs = await inline.get_keyboard_langs('from')
    await msg.answer('Выберите с какого языка хотите перевести',
                     reply_markup=keyboard_langs)


@router.callback_query(F.data.startswith('from:'))
async def translate(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    await state.set_state(Form.code_from)
    code = callback.data.split(":")[1]
    await state.update_data(code_from=code)

    keyboard_langs = await inline.get_keyboard_langs('to')

    await callback.message.edit_text('Теперь выберите язык на который хотите перевести',
                                    reply_markup=keyboard_langs)


@router.callback_query(F.data.startswith('to:'))
async def translate(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    await callback.message.edit_text('Подождите идет обработка...')

    await state.set_state(Form.code_to)
    code = callback.data.split(":")[1]
    await state.update_data(code_to=code)

    data = await state.get_data()
    await state.clear()

    text_to_translate = data['text']
    code_to = data['code_to']
    code_from = data['code_from']

    translated_text = tr.translate(text_to_translate, code_from, code_to)

    await callback.message.edit_text(f'{translated_text}')