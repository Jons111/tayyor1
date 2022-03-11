from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

torrent = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='uTorrentni yuklash'),
            KeyboardButton(text='Back 🔙')
        ]

    ],
    resize_keyboard=True

)