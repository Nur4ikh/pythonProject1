from aiogram import types


async def education(message: types.Message):
    kb = types.ReplyKeyboardMarkup()
    kb.add(
        types.KeyboardButton("Немецкий язык"),
        types.KeyboardButton("Английский язык"),
    )
    await message.answer(
        "Выберите интересующее вас направление:",
        reply_markup=kb
    )

async def show_back_end(message: types.Message):
    await message.answer("Самое лучшее направление")