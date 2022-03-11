from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



ps_1: ReplyKeyboardMarkup=ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text='👉 Biohazard 2 Prototype 👈'),
             KeyboardButton(text='👉 Supermen 👈')
        ],
        [
             KeyboardButton(text='👉 2:1 Nightmare 👈'),
             KeyboardButton(text='🦇 Batman Forever 🦇')
        ],
        [
             KeyboardButton(text='Back 🔙')
        ]

    ],
    resize_keyboard=True

)

