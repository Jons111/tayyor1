from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



ps_2: ReplyKeyboardMarkup=ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text='⚽ Pro Evolution Soccer 2019 ⚽'),
             KeyboardButton(text='👉 Gta san andreas 👈')
        ],
        [
             KeyboardButton(text='👉 Astro Boy 👈'),
             KeyboardButton(text='👉 X-Men 👈')
        ],
        [
             KeyboardButton(text='Back 🔙')
        ]

    ],
    resize_keyboard=True

)