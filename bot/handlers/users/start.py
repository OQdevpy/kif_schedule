import sqlite3
import time

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart


from data.config import ADMINS
from loader import dp, db, bot

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from keyboards.default.defoult_btn import back_btn, menu_btn, message_phone, menu_btn_ru
from keyboards.inline.inline_btn import lang_btn


txt = """
Universitetda korrupsiyaga oid sizni qiynayotgan muammo yoki voqeaga oid murojatingiz bo`lsa marhamat qilib ushbu botga yo'llashingiz mumkin.
    """

txt_ru = """
Если у вас есть жалоба или заявление по коррупции в университете, вы можете отправить его в этот бот.
    """
@dp.message_handler(text="/start")
async def start_bot(message: types.Message, state=FSMContext):
   
       
    try:
        user = db.select_user(telegram_id=message.from_user.id)
        if not user:

            if message.from_user.username:
                    username = message.from_user.username
            else:
                    username = ""
            db.add_bot_user(telegram_id=message.from_user.id, full_name=message.from_user.full_name, user_name=username)
            
            await message.answer("Assalomu alaykum, botga xush kelibsiz!\nЗдравствуйте, добро пожаловать в бот!")
            
            await message.answer("O’zingizga qulay tilni tanlang!\nВыберите удобный Вам язык!", reply_markup=lang_btn)
            
        else:
            if user[7] == "uz":
                await message.answer_animation(animation="CgACAgIAAxkBAAIBVmUrom5MlQGUprxFX05vPLDTv2K0AAIjNwACWF9gSff17npwgdPWMAQ", caption="Assalom alaykum! Siz Toshkent xalqaro moliyaviy boshqaruv va texnologiyalar universiteti korrupsiyaga qarshi kurashish departamentiga murojaat qildingiz, sizga qanday yordam bera olishimiz mumkin?", reply_markup=menu_btn)
                time.sleep(2)
                await message.answer(txt)
            else:
                await message.answer_animation(animation="CgACAgIAAxkBAAIBVmUrom5MlQGUprxFX05vPLDTv2K0AAIjNwACWF9gSff17npwgdPWMAQ", caption="Здравствуйте! Вы обратились в департамент по борьбе с коррупцией Ташкентского университета финансового управления и технологий, как мы можем вам помочь?", reply_markup=menu_btn_ru)
                time.sleep(2)
                await message.answer(txt_ru)
                
    except Exception as err:
        print(err)
    
@dp.callback_query_handler(state="*", text="uzbek")
async def get_all_users(call: types.CallbackQuery, state:FSMContext):
    await call.message.answer(txt, reply_markup=menu_btn)
        
    db.update_user_language(telegram_id=call.from_user.id, language="uz")
    await call.message.delete()
    await state.finish()

@dp.callback_query_handler(state="*", text="russian")
async def get_all_users(call: types.CallbackQuery, state:FSMContext):
    
    await call.message.answer(txt_ru, reply_markup=menu_btn_ru)
    
    db.update_user_language(telegram_id=call.from_user.id, language="ru")
    await call.message.delete()
    await state.finish()
    
    
@dp.message_handler(text="🇺🇿/🇷🇺 Bot tilini sozlash")
async def get_all_users(message: types.Message):
    await message.answer("Tilni tanlang", reply_markup=lang_btn)

@dp.message_handler(text="🇺🇿/🇷🇺 Настройка языка бота")
async def get_all_users(message: types.Message):
    await message.answer("Выберите удобный Вам язык!", reply_markup=lang_btn)
    
    