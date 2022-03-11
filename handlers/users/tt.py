from aiogram import types

from keyboards.default.menu import asosiy_menu
from loader import dp
from keyboards.default.tor import torrent


# Echo bot
@dp.message_handler(text='uTorrent')
async def bot_echo(message: types.Message):
    await message.answer(text='Marhamat yuklab olishingiz mumkin',reply_markup=torrent)


@dp.message_handler(text='Back 🔙')
async def bot_echo(message: types.Message):
    await message.answer(text='orqaga',reply_markup=asosiy_menu)