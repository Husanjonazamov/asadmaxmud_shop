# aiogram import
from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand, MenuButtonWebApp, WebAppInfo
from aiogram.filters import Command


# kode import
from utils import texts
from utils.env import BOT_TOKEN, WEBAPP_URL
from utils.services import createUser, getUser

import asyncio
import logging

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


logging.basicConfig(level=logging.INFO) 



@dp.message(Command('start'))
async def start_handler(message: types.Message):
    first_name = message.from_user.first_name 
    user_id = message.from_user.id
    
    user = getUser(user_id)
    
    if not user:
        new_user = {
            'user_id': user_id,
            'first_name': first_name
            }
        createUser(new_user)
        
    await message.answer(texts.START.format(first_name))

    

async def set_bot_menu():
    await bot.set_my_commands(
        commands=[
            BotCommand(command="start", description="Boshlash"),
        ]
    )
    
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text="Bozor", 
            web_app=WebAppInfo(url=WEBAPP_URL) 
        )
    )

async def main():
    await set_bot_menu()
    await dp.start_polling(bot)

asyncio.run(main())
