import logging

from aiogram import executor
from aiogram.dispatcher.filters import Text

from config import dp
from handlers.about_us import about_us
from handlers.education import education, show_back_end
from handlers.review import review
from handlers.start import echo, send_picture, start

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # dp.register_callback_query_handler(about_us, Text('about'))
    dp.register_callback_query_handler(about_us, lambda cb: cb.data == 'about')
    dp.register_callback_query_handler(review, lambda cb: cb.data == 'review')

    dp.register_message_handler(education, commands=["edu"])
    dp.register_message_handler(show_back_end, Text("Немецкий язык"))
    dp.register_message_handler(show_back_end, Text("Английский язык"))

    dp.register_message_handler(send_picture, commands=["pic"])
    dp.register_message_handler(start, commands=["start"])

    dp.register_message_handler(echo)

    # в самом конце
    executor.start_polling(dp)
