from aiogram import types
from db.queries_1 import get_product
from pprint import pprint
async def product(messages: types.Message):
    """Продукты"""
    kb = types.ReplyKeyboardMarkup()
    kb.add(
        types.KeyboardButton("Продукты"),
    )
    await messages.answer(
        "Нажмите на кнопку чтобы увидеть продукты:",
        reply_markup=kb
    )
async def about_product(messages: types.Message):
    product = get_product()
    pprint(product)
    await messages.answer(f'Здесь представлены продукты и их цены: \n{product}')

