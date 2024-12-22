from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand, MenuButtonWebApp, WebAppInfo
from aiogram.filters import Command
import asyncio

API_TOKEN = "7178118588:AAHr3QkdJxksP_xtCKgrMPNFLeOpkHJqNWc"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


WEBAPP_URL = "https://www.youtube.com/"


@dp.message(Command('start'))
async def start_handler(message: types.Message):
    user_first_name = message.from_user.first_name 
    await message.answer(f"Assalomu alaykum, {user_first_name}!")



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
