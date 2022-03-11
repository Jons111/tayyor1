from aiogram import types

from keyboards.default.menu import asosiy_menu
from loader import dp
from keyboards.default.oyinlar_button import oyinlar



# Echo bot
@dp.message_handler(text='Kompyuter oyinlar 💻')
async def bot_echo(message: types.Message):
    await message.answer(text='Oyinlarni tanlang',reply_markup=oyinlar)





@dp.message_handler(text='Back 🔙')
async def bot_echo(message: types.Message):
    await message.answer(text='orqaga',reply_markup=asosiy_menu)
