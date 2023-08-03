from aiogram import types
from pprint import pprint
from config import bot


async def check_author_is_admin(message: types.Message):
    member_type = await message.chat.get_member(message.from_user.id)
    pprint(member_type)
    return not member_type["status"] != "member"


async def example(message: types.Message):
    print(f"{message.chat.type=}")
    print(f"{message.reply_to_message=}")

    if message.chat.type != "private":
        await message.answer("Это сообщение было отправлерно не в ЛС")
    else:
        await message.answer("Этот бот работает только в группе")


bad_words = ("дурак", "лох")


async def catch_bad_words(message: types.Message):
    if message.chat.type != "private":
        for word in bad_words:
            if word in message.text.lower():
                user_info = await bot.get_chat_member(message.chat.id, message.from_user.id)
                if user_info.status in ['administrator', 'creator']:
                    await message.answer("Предупреждаю в группе соблюдать правила")
                else:
                    await message.answer('Вы были забанены за нарушения правил в группе')
                    await bot.kick_chat_member(message.chat.id, message.from_user.id)
                    break