import logging
from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv
from database import Database
from buttons import mainButton, menuButton, orderButton

load_dotenv()


API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    firstName = message.from_user.first_name
    lastName = message.from_user.last_name
    username = message.from_user.username
    chatId = str(message.chat.id)

    checkQuery = f"""SELECT * FROM users WHERE chat_id = '{chatId}'"""
    if len(Database.connect(checkQuery, "select")) >= 1:
        print(f"{username}")
        await message.answer(f"""Hello @{username}""", reply_markup=mainButton)
    else:
        print(f"""{firstName} started bot""")
        query = f"""INSERT INTO users(first_name, last_name, username, chat_id) VALUES('{firstName}', '{lastName}', '{username}', '{chatId}')"""
        print(f"""{username} {Database.connect(query, "insert")} database""")
        print(f"{username}")
        await message.answer(f"""Hello @{username}""", reply_markup=mainButton)


@dp.message_handler(commands=["data"])
async def select(message: types.Message):
    chatID = message.chat.id
    selectQuery = f"SELECT * FROM users WHERE chat_id = '{chatID}'"
    data = Database.connect(selectQuery, "select")
    await message.reply(f"""{data}""")


@dp.message_handler(lambda message: message.text == "🍽Menu")
async def menu(message: types.Message):
    await message.answer("Choose Menu:", reply_markup=menuButton)


@dp.message_handler(lambda message: message.text == "Back")
async def backMenu(message: types.Message):
    await message.answer("Main Menu:", reply_markup=mainButton)


@dp.message_handler(lambda message: message.text == "🛍My orders")
async def myOrders(message: types.Message):
    await message.answer("Your Orders:", reply_markup=orderButton)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

