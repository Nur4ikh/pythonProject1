from aiogram import types

from handlers.constants import HELLO_TEXT


# @dp.message_handler(commands=["start"])
async def start(message: types.Message):
    # await message.answer("Привет")
    print(f"{message.from_user=}")
    # await message.reply(f"Привет, {message.from_user.username}")

    kb = types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton("Наш сайт",
                                   url="https://delfitraining.com/"),
        types.InlineKeyboardButton("О нас", callback_data='about')
    )
    kb.add(types.InlineKeyboardButton("Отзывы",
                                      callback_data='review'))

    await message.reply(HELLO_TEXT, reply_markup=kb)


# @dp.message_handler(commands=["pic"])
async def send_picture(message: types.Message):
    """Отправляет картинку пользователю"""
    # Doc String
    with open('images/germany.jpg', 'rb') as photo:
        await message.answer_photo(
            photo,
            caption="Мечты сбываются вместе с нами!")


# @dp.message_handler()
async def echo(message: types.Message):
    """Эхо, функция, которая отправляет пользователю"""
    await message.answer(message.text)