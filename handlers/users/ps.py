from aiogram import types
from aiogram.types import ContentType, InputFile
from loader import bot

from loader import dp
 # Echo bot




@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='👉 Biohazard 2 Prototype 👈')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/Biohazard 2 Prototype.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='👉 Supermen 👈')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/Supermen.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='👉 2:1 Nightmare 👈')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/2 Nightmare .torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='🦇 Batman Forever 🦇')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/Batman Forever.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='⚽ Pro Evolution Soccer 2019 ⚽')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/Pro Evolution Soccer 2019.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)

@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='👉 Gta san andreas 👈')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/Gta san andreas.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)


@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='👉 Astro Boy 👈')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/Astro Boy.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='👉 X-Men 👈')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/X-Men.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)




@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='👉 Gta 4 👈')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/Gta 4.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)




@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='🔫 Call of Duty 4:Modern Warfare 🔫')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/Call of Duty 4 Modern Warfare.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)



@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='🧟 Resident evil 5 🧟')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/Resident evil 5.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)




@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='👉 Transformers 👈')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/Transformers.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)





@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='🧟 Resident evil 3 remake 🧟')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/Resident evil 3 remake.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)




@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='🔫 The Wicher 3 🔫')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/The Wicher 3.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)




@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='🦍 Peter Jacksons King Kong 🦍')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/Peter Jacksons King Kong.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)






@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()

    await message.answer(message.text)

@dp.message_handler(text='🔫 Hitman 🔫')
async def bot_echo(message: types.Message):

    a = InputFile(path_or_bytesio='documents/Hitman.torrent')
    user_id=message.from_user.id

    await bot.send_document(chat_id=user_id,document=a)





@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.answer_document(document='https://t.me/c/1268795293/5')



@dp.message_handler(text='uTorrentni yuklash')
async def bot_echo(message: types.Message):
        await message.reply_document(document='https://t.me/jghcfhghcfg/5')

