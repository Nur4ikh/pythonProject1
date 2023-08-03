from aiogram import executor
from handlers.user_form import register_survey_handlers
from aiogram.dispatcher.filters import Text
from config import dp, scheduler
from handlers.user_form import cmd_start
# from handlers.notify import notify
# from handlers.group_admin import catch_bad_words, pin_message_in_group, ban_group_user
from handlers.product import product, about_product

from db.queries_1 import (
    create_table,
    drop_tables,
    init_db,
    populate_tables)
async def bot_start(_):
    init_db()
    drop_tables()
    create_table()
    populate_tables()

# dp.register_message_handler(notify, commands='notify')


# dp.register_message_handler(
#         pin_message_in_group, commands="pin", commands_prefix="!"
#     )
# dp.register_message_handler(ban_group_user, commands="ban", commands_prefix="!")
# dp.register_message_handler(cmd_start, commands=["surv"])
dp.register_message_handler(product, commands=["pro"])
dp.register_message_handler(about_product, Text('Продукты'))

register_survey_handlers(dp)

# dp.register_message_handler(catch_bad_words)


# scheduler.start()
executor.start_polling(
        dp,
        on_startup=bot_start,
        skip_updates=True
    )

