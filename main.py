from aiogram import executor
from handlers.user_form import register_survey_handlers

from config import dp, scheduler
from handlers.user_form import cmd_start
from handlers.notify import notify
from handlers.group_admin import catch_bad_words, pin_message_in_group, ban_group_user

# dp.register_message_handler(notify, commands='notify')


# dp.register_message_handler(
#         pin_message_in_group, commands="pin", commands_prefix="!"
#     )
# dp.register_message_handler(ban_group_user, commands="ban", commands_prefix="!")
dp.register_message_handler(cmd_start, commands=["surv"])
register_survey_handlers(dp)

# dp.register_message_handler(catch_bad_words)


# scheduler.start()
executor.start_polling(dp)
