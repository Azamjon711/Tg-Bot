from aiogram import types

keyButton = types.InlineKeyboardMarkup(row_width=3)
button1 = types.InlineKeyboardButton(text="🇺🇿", callback_data="uz")
button2 = types.InlineKeyboardButton(text="🇬🇧", callback_data="eng")
button3 = types.InlineKeyboardButton(text="🇷🇺", callback_data="ru")
keyButton.add(button1, button2, button3)