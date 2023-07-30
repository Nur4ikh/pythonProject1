from os import getenv

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler


load_dotenv()
storage = MemoryStorage()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=storage)
scheduler = AsyncIOScheduler()
