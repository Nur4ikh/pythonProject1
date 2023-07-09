from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
from os import getenv


load_dotenv()

bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=["picture"])
async def send_picture(message: types.Message):
    with open('images/germany.jpg', 'rb') as photo:
        await message.answer_photo(
            photo,
            caption="Ich möchte nach Deutschland fliegen😍")

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    # await message.answer("Привет")
    print(f"{message.from_user=}")
    await message.reply(f"Привет, {message.from_user.username} как ваше настроение? "
                        f"Меня создал НУРСУЛТАН!")

@dp.message_handler(commands=["myinfo"])
async def my_info(message: types.Message):
    print(f"{message.from_user=}")
    await message.reply(f"Ваш ID: {message.from_user.id}\nВаше имя: {message.from_user.first_name}\n"
                        f"Ваш Никнейм: {message.from_user.username}")

@dp.message_handler()
async def echo(message: types.Message):
    print(f"{message.from_user}")
    await message.reply(f"Нажмите на Меню чтобы увидеть комманды!")


if __name__ == "__main__":
    executor.start_polling(dp)
