import time
from aiogram import types
from data.config import ADMINS
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from keyboards.default.defoult_btn import back_btn, menu_btn, message_phone, student_documents_btn
from data.api import get_user_by_id, create_user, get_sources

@dp.message_handler(text="/start")
async def start_bot(message: types.Message, state=FSMContext):
    user_ = message.from_user
    user = get_user_by_id(user_.id)
    if user != 200:
        username = user_.username if user_.username else None
        create_user(user_.id, username, user_.full_name, True)
    await message.answer(f"Assalomu alaykum {user_.full_name}", reply_markup=menu_btn)

@dp.message_handler(text="📆 Dars jadvali")
async def schedule_func(message: types.Message):
    await message.answer("Dars jadvali", reply_markup=menu_btn)



@dp.message_handler(text="📄 Talaba xujjatlari")
async def student_documents(message: types.Message):
    docs = get_sources()
    await message.answer("Talaba xujjatlari", reply_markup=student_documents_btn(docs))

@dp.message_handler(text="🔙 Back")
async def back(message: types.Message):
    await message.answer("Asosiy menu", reply_markup=menu_btn)

