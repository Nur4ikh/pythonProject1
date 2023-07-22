from pprint import pprint

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class UserForm(StatesGroup):
    name = State()
    age = State()
    gender = State()


async def start_survey(message: types.Message):
    await UserForm.name.set()
    await message.answer("Как вас зовут?")


async def process_name(message: types.Message, state: FSMContext):
    msg = message.text
    if msg.isdigit():
        await message.answer("Используйте буквы!")
    elif len(msg) > 15:
        await message.answer("Имя не должно превышать 15 символов!")
    else:
        await UserForm.next()

        await message.answer("Введите ваш возраст:")


async def process_age(message: types.Message, state: FSMContext):
    msg = message.text
    if not msg.isdigit():
        await message.answer("Введите число")
    elif int(msg) < 15 or int(msg) > 99:
        await message.answer("Введите число от 15 до 99")
    else:
        await UserForm.next()

        kb = types.ReplyKeyboardMarkup()
        kb.add("от 2 до 4 лет", "от 5 до 7 лет")
        await message.answer("Какой у вас опыт в программировании?:", reply_markup=kb)


async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text

    await state.finish()

    await message.answer("Спасибо, мы скоро свяжемся с вами!")


def register_survey_handlers(dp: Dispatcher):
    dp.register_message_handler(start_survey, commands=["surv"])
    dp.register_message_handler(process_name, state=UserForm.name)
    dp.register_message_handler(process_age, state=UserForm.age)
    dp.register_message_handler(process_gender, state=UserForm.gender)