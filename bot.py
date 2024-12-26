from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand, MenuButtonWebApp, WebAppInfo

from aiogram.filters import Command

from utils import texts
import asyncio
import logging
from utils.env import BOT_TOKEN, WEBAPP_URL




bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    """Start buyrug'i"""
    first_name = message.from_user.first_name
    await message.answer(text=texts.START.format(first_name))
    await bot.set_chat_menu_button(
    menu_button=MenuButtonWebApp(
        text="Bozor",
        web_app=WebAppInfo(url=WEBAPP_URL) 
    )
)




async def main():
    await dp.start_polling(bot)


asyncio.run(main())
