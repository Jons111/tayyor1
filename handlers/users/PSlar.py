from aiogram import types

from loader import dp
from keyboards.default.pslar import pslar


# Echo bot
@dp.message_handler(text='PSlar uchun 🎮')
async def bot_echo(message: types.Message):
    await message.answer(text='Ozingizga kerakligini tanlang',reply_markup=pslar)
