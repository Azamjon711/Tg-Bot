from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from database import Database

mainButton = ReplyKeyboardMarkup([
    [KeyboardButton("🍽Menu")],
    [KeyboardButton("🛍My orders")],
    [KeyboardButton("✍️Leave Feedback"), KeyboardButton("⚙️Settings")]
], resize_keyboard=True)

# mainButton.add(KeyboardButton("Menu"))
# mainButton.add(KeyboardButton("My orders"))
# mainButton.add(KeyboardButton("Leave Feedback"))
# mainButton.add(KeyboardButton("Settings"))


# menuButton = ReplyKeyboardMarkup([
#     [KeyboardButton("Menu 1"), KeyboardButton("Menu 2")],
#     [KeyboardButton("Menu 3"), KeyboardButton("Menu 4")],
#     [KeyboardButton("Menu 5"), KeyboardButton("Menu 6")],
#     [KeyboardButton("Back")]
#
# ], resize_keyboard=True)

# menuButton.add(KeyboardButton("Menu 1"))
# menuButton.add(KeyboardButton("Menu 2"))
# menuButton.add(KeyboardButton("Menu 3"))
# menuButton.add(KeyboardButton("Menu 4"))
# menuButton.add(KeyboardButton("Back"))

menuButton = ReplyKeyboardMarkup(resize_keyboard=True)
query = "SELECT * FROM menu"
for i in Database.connect(query, "select"):
    menuButton.add(KeyboardButton(i[1]))
menuButton.add(KeyboardButton("Back"))

# orderButton = ReplyKeyboardMarkup([
#     [KeyboardButton("Order 1"), KeyboardButton("Order 2")],
#     [KeyboardButton("Order 3"), KeyboardButton("Order 4")],
#     [KeyboardButton("Order 5"), KeyboardButton("Order 6")],
#     [KeyboardButton("Back")]
#
# ], resize_keyboard=True)

orderButton = ReplyKeyboardMarkup(resize_keyboard=True)
query = "SELECT * FROM orders"
for i in Database.connect(query, "select"):
    orderButton.add(KeyboardButton(i[1]))
orderButton.add(KeyboardButton("Back"))


settingButton = ReplyKeyboardMarkup(resize_keyboard=True)
settingButton.add(KeyboardButton("Change language"))
settingButton.add(KeyboardButton("Back"))


feedbackButton = ReplyKeyboardMarkup(resize_keyboard=True)
feedbackButton.add(KeyboardButton("📲Phone number"))
feedbackButton.add(KeyboardButton("Back"))
