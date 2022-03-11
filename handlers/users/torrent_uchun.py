from aiogram import types
from aiogram.types import ContentType, InputFile
from loader import bot

from loader import dp
 # Echo bot


@dp.message_handler(content_types=ContentType.LOCATION)
async def bot_echo(message: types.Message):
    await message.location.download()

    await message.answer(message.text)

@dp.message_handler(text='FarCry5')
async def bot_echo(message: types.Message):

    a= InputFile(path_or_bytesio='documents/FarCry_5.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)