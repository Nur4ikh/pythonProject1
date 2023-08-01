from aiogram import executor
from handlers.start import echo

from config import dp, scheduler
from handlers.user_form import register_survey_handlers
from handlers.notify import notify

dp.register_message_handler(notify, commands='notify')

register_survey_handlers(dp)

dp.register_message_handler(echo)

scheduler.start()
executor.start_polling(dp)
