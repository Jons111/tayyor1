from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



ps_3: ReplyKeyboardMarkup=ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text='👉 Gta 4 👈'),
             KeyboardButton(text='🔫 Call of Duty 4:Modern Warfare 🔫')
        ],
        [
             KeyboardButton(text='🧟 Resident evil 5 🧟'),
             KeyboardButton(text='👉 Transformers 👈')

        ],
        [
             KeyboardButton(text='Back 🔙')
        ]

    ],
    resize_keyboard=True

)