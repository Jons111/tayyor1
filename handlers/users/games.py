from aiogram import types
from aiogram.types import ContentType, InputFile
from loader import bot

from loader import dp
 # Echo bot


@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()
    document=message.document.file_id
    await message.answer(text=f'oyin yuborildi {document}')

@dp.message_handler(text='👉 FarCry5 👈')
async def bot_echo(message: types.Message):

    a= InputFile(path_or_bytesio='documents/FarCry_5.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)





@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='👉 Gta 5 👈')
async def bot_echo(message: types.Message):

    a= InputFile(path_or_bytesio='documents/Gta_5.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='🧟 Metro exodus 🧟')
async def bot_echo(message: types.Message):

    a= InputFile(path_or_bytesio='documents/metro_exodus.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)


@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='🔫 Call of Duty Modern Warfare 2 🔫')
async def bot_echo(message: types.Message):

    a= InputFile(path_or_bytesio='documents/Call_ of_ Duty_ modern_warfare_2.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)


@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='🏎 Need for Speed Most Wanted 🏎')
async def bot_echo(message: types.Message):

    a= InputFile(path_or_bytesio='documents/Need for Speed Most Wanted.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)









@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='🧟‍ Resident evil 4 🧟')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/Resident evil 4.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='🏎 Blur 🏎')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/Blur.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)

@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='🥷 Assassins creed III 🥷')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/Assassins creed III.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)