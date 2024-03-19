from aiogram import types

keyButton = types.InlineKeyboardMarkup(row_width=3)
changeLangButton1 = types.InlineKeyboardButton(text="🇺🇿", callback_data="uz")
changeLangButton2 = types.InlineKeyboardButton(text="🇬🇧", callback_data="eng")
changeLangButton3 = types.InlineKeyboardButton(text="🇷🇺", callback_data="ru")
keyButton.add(changeLangButton1, changeLangButton2, changeLangButton3)

addNewAdminButton = types.InlineKeyboardMarkup(row_width=2)
inlineAdminButton1 = types.InlineKeyboardButton(text="name", callback_data="admin_name")
inlineAdminButton2 = types.InlineKeyboardButton(text="chat_id", callback_data="admin_id")
addNewAdminButton.add(inlineAdminButton1,inlineAdminButton2)