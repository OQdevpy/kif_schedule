from aiogram import types
from data.config import ADMINS


from loader import dp, db, bot

from keyboards.default.defoult_btn import menu_btn


@dp.message_handler( user_id=ADMINS)
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    await message.answer(message.text, reply_markup=menu_btn)
    
    
@dp.message_handler()
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    await message.answer(message.text, reply_markup=menu_btn)

    