from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



pslar: ReplyKeyboardMarkup=ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text='PS 1'),
             KeyboardButton(text='PS 2')
        ],
        [
            KeyboardButton(text='PS 3'),
            KeyboardButton(text='PS 4')
        ],
        [
            KeyboardButton(text='Back 🔙')
        ]




    ],
    resize_keyboard=True

)