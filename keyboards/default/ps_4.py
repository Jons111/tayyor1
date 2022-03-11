from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



ps_4: ReplyKeyboardMarkup=ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text='🧟 Resident evil 3 remake 🧟'),
             KeyboardButton(text='🔫 The Wicher 3 🔫')
        ],
        [
             KeyboardButton(text='🦍 Peter Jacksons King Kong 🦍'),
             KeyboardButton(text='🔫 Hitman 🔫')
        ],
        [
             KeyboardButton(text='Back 🔙')
        ]

    ],
    resize_keyboard=True

)