from aiogram import types
from config import scheduler, bot


async def notify(message: types.Message):
    user_id = str(message.from_user.id)
    if scheduler.get_job(user_id) is not None:
        await message.answer('you use notify')
    else:
        # scheduler.add_job(
        #     send_notify,
        #     'interval',
        #     seconds=7,
        #     id=user_id,
        #     kwargs={'user_id': message.from_user.id}
        # )
        # scheduler.add_job(
        #     send_notify,
        #     'date',
        #     run_date=datetime(2023, 7, 27, 17, 21),
        #     kwargs={'user_id': message.from_user.id}
        # )
        scheduler.add_job(
            send_notify,
            'cron',
            hour=18,
            minute=9,
            second=10,
            kwargs={'user_id': message.from_user.id}
        )
        await message.answer('okey')


async def send_notify(user_id: int):
    await bot.send_message(
        chat_id=user_id,
        text='Покорми кота!'
    )