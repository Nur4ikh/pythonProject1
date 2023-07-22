import logging

from aiogram import executor
from handlers.start import echo

from config import dp
from handlers.user_form import register_survey_handlers


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    register_survey_handlers(dp)

    dp.register_message_handler(echo)

    # в самом конце
    executor.start_polling(dp)
