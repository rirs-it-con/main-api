import logging
import os
from aiogram import Bot
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("TOKEN")

bot = Bot(token=BOT_TOKEN)
