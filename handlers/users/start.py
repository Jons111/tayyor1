from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import asosiy_menu
from loader import dp


@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    # ism = message.from_user.first_name
    # fam = message.from_user.last_name
    # user_name = message.from_user.username
    # user_id = message.from_user.id
    # db.user_qoshish(ism=ism,fam=fam,username=user_name,tg_id=user_id)
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!  "
                              f"botga hush kelibsiz,bizning bot sizga yordam beradi degan umiddamiz,bizning kompyuter oyinlarimiz uTorrent formatda",reply_markup=asosiy_menu)
