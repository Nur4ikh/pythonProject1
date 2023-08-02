from pprint import pprint

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from db.queries_1 import save_user_results

class UserForm(StatesGroup):
    name = State()
    age = State()
    gender = State()


async def cmd_start(message: types.Message):
    # Переходим в первое состояние
    await UserForm.name.set()
    await message.reply("Привет! Как тебя зовут?")


async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    name = message.text
    if not name.isalpha():
        await message.answer('Пожалуйста введите букву')
    elif len(str(name)) < 2 or len(str(name)) > 15:
        await message.answer("Имя должен состоять из 2-х букв и выше,"
                             "и меньше 15 букв")
    else:
        async with state.proxy() as data:
            data['name'] = str(name)

        # Переходим во второе состояние
        await UserForm.next()
        await message.reply("Сколько тебе лет?")


async def process_age(message: types.Message, state: FSMContext):
    msg = message.text
    if not msg.isdigit():
        await message.answer("Пожалуйста, введите возраст числом.")
    elif int(msg) < 15 or int(msg) > 99:
        await message.answer("Анкета создается для тех кому 15 до 99")
    else:
        async with state.proxy() as data:
            data["age"] = message.text
            # pprint(data.as_dict())

        # Переходим в третье состояние
        kb = types.ReplyKeyboardMarkup()
        kb.add("Мужской", "Женский")
        await UserForm.next()
        await message.reply("Укажи свой пол:", reply_markup=kb)


async def process_gender(message: types.Message, state: FSMContext):
    gender = message.text

    if gender not in ('Мужской', 'Женский'):
        await message.reply("Пожалуйста, нажмите на кнопку")
    else:
        async with state.proxy() as data:
            data['gender'] = message.text
            # pprint(data.as_dict())

            save_user_results(data.as_dict())

        await state.finish()
#
#         data = await state.get_data()
        await message.answer(f"Спасибо за заполнение анкеты!\n"
                             f"Ваши данные:\n"
                             f"Имя: {data['name']}\n"
                             f"Возраст: {data['age']}\n"
                             f"Пол: {data['gender']}\n"
                             f"До свидания!")


def register_survey_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["surv"])
    dp.register_message_handler(process_name, state=UserForm.name)
    dp.register_message_handler(process_age, state=UserForm.age)
    dp.register_message_handler(process_gender, state=UserForm.gender)
