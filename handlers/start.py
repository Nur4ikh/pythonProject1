from aiogram import types




async def echo(message: types.Message):
    """Эхо, функция, которая отправляет пользоватео"""
    await message.answer(message.text)