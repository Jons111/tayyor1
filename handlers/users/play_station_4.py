from aiogram import types

from keyboards.default.menu import asosiy_menu
from loader import dp
from keyboards.default.ps_4 import ps_4


# Echo bot
@dp.message_handler(text='PS 4')
async def bot_echo(message: types.Message):
    await message.answer(text='Oyinlarni tanlang',reply_markup=ps_4)



@dp.message_handler(text='Back 🔙')
async def bot_echo(message: types.Message):
    await message.answer(text='orqaga',reply_markup=asosiy_menu)
