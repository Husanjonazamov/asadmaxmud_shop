from aiogram import Bot, Dispatcher, types
from aiogram.types import MenuButtonWebApp, WebAppInfo
from aiogram.filters import Command
import asyncio
import logging

from utils import texts
from utils.services import getUser, createUser
from utils.env import BOT_TOKEN, WEBAPP_URL  


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    """Start buyrug'i"""
    firstname = message.from_user.first_name
    user_id = message.from_user.id
    
    get_user = getUser(user_id)
    
    if not get_user:
        user = {
            'user_id': user_id,
            'firstname': firstname
        }
        createUser(user)
        
    await message.answer(text=texts.START.format(firstname))
    
    user_webapp_url = f"{WEBAPP_URL}?user_id={user_id}"
    
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text="Bozor", 
            web_app=WebAppInfo(url=user_webapp_url) 
        )
    )

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
