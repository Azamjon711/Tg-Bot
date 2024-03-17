import logging
from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv
from database import Database
from buttons import mainButton, menuButton, orderButton, settingButton, feedbackButton
from keyboard import keyButton

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


@dp.message_handler(lambda message: message.text == "⚙️Settings")
async def settings(message: types.Message):
    await message.answer("Settings:", reply_markup=settingButton)


@dp.message_handler(lambda message: message.text == "✍️Leave Feedback")
async def feedback(message: types.Message):
    await message.answer("Leave feedback:", reply_markup=feedbackButton)


@dp.message_handler(lambda message: message.text == "Change language")
async def changeLang(message: types.Message):
    await message.answer("Choose language:", reply_markup=keyButton)


@dp.callback_query_handler(lambda call: call.data == "uz" or call.data == "eng" or call.data == "ru")
async def changedLangQuery(query: types.CallbackQuery):
    if query.data == "uz" or query.data == "eng" or query.data == "ru":
        await query.answer("Language successfully changed")


@dp.message_handler(lambda message: message.text == "First meal")
async def firstMealImage(message: types.Message):
    urlPhoto = "https://avatars.mds.yandex.net/i?id=5a8cda3d2538aa40aa6858032abee1b65eceffda-10555703-images-thumbs&n=13"
    caption = "First meals:"
    await bot.send_photo(message.chat.id, photo=urlPhoto, caption=caption)


@dp.message_handler(lambda message: message.text == "Second meal")
async def secondMealImage(message: types.Message):
    urlPhoto = "https://avatars.mds.yandex.net/i?id=8a0ecbc2a0717269002180e84299148c6d19dd34-10136504-images-thumbs&n=13"
    caption = "Second meals:"
    await bot.send_photo(message.chat.id, photo=urlPhoto, caption=caption)


@dp.message_handler(lambda message: message.text == "Snacks")
async def snacksImage(message: types.Message):
    urlPhoto = "https://avatars.mds.yandex.net/i?id=78b18133c2c8608e2eb6069a3a8d33d802e5be58-10948701-images-thumbs&n=13"
    caption = "Snacks:"
    await bot.send_photo(message.chat.id, photo=urlPhoto, caption=caption)


@dp.message_handler(lambda message: message.text == "Appetizers")
async def appetizersImage(message: types.Message):
    urlPhoto = "https://avatars.mds.yandex.net/i?id=7079f1857968f626212040ec8c85569b9f16eb05-5283588-images-thumbs&n=13"
    caption = "Appetizers:"
    await bot.send_photo(message.chat.id, photo=urlPhoto, caption=caption)


@dp.message_handler(lambda message: message.text == "Beverages")
async def beveragesImage(message: types.Message):
    urlPhoto = "https://avatars.mds.yandex.net/i?id=4d9a5be1624e8db93456e542e5bc4be9acccbcc3-12521952-images-thumbs&n=13"
    caption = "Beverages:"
    await bot.send_photo(message.chat.id, photo=urlPhoto, caption=caption)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
