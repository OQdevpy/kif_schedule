import asyncio
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.defoult_btn import back_btn,  menu_btn
from aiogram import types, utils

from data.config import ADMINS
from loader import dp, db, bot

from datetime import datetime

from aiogram.dispatcher import FSMContext


@dp.message_handler(CommandStart(), user_id=ADMINS)
async def bot_start(message: types.Message):
    user_id = message.from_user.id    
    await message.answer("Xush kelibsiz Admin!", reply_markup=menu_btn)
  
            
            
@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message, state: FSMContext):
    await message.answer("Foydalanuvchilarga reklamani forward qilish uchun biror kanaldan postni forward qilib yuboring...", reply_markup=back_btn)
    await state.set_state("forward_message")

@dp.message_handler(state="forward_message", text ="🔙 Back")
async def input_password(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"Asosiy panel",reply_markup=menu_btn)
    
@dp.message_handler(state="forward_message", content_types=types.ContentTypes.ANY)
async def forward_post(message: types.Message, state=FSMContext):
    # print(message)
    # print(post_id, channel)
    
    # forward message to users 
    if message.forward_from_chat:
        all_users = db.select_all_users()
        failed_users = 0
        
        for user in all_users:
            try:
                # await bot.forward_message(chat_id=user[1], from_chat_id=str(channel), message_id=post_id)
                await message.forward(chat_id=user[1])
                await asyncio.sleep(0.05)
            except Exception as err:
                failed_users += 1
                continue
    else:
        all_users = db.select_all_users()
        failed_users = 0
        
        for user in all_users:
            try:
                await message.send_copy(chat_id=user[1])
                await asyncio.sleep(0.05)
            except Exception as err:
                failed_users += 1
                continue
    await message.answer(f"Barcha userlarga xabar yuborildi\n\nJami userlar: {len(all_users)}\n\nXabar yetib bormadi: {failed_users}", reply_markup=menu_btn)
    await state.finish()
    
@dp.message_handler(text="/about", user_id=ADMINS)
async def get_about(message: types.Message):
    if message.reply_to_message:
        if message.reply_to_message.forward_sender_name:
            user = db.select_user(tg_name=message.reply_to_message.forward_sender_name)
        else:
            user = db.select_user(telegram_id=message.reply_to_message.forward_from.id)
        await message.reply(f"User haqida ma'lumotlar:\n\nID: {user[0]}\nTelegram ID: {user[1]}\nNick Name: {user[2]}\nFull Name: {user[3]}\nTelegram Username: {user[5]}\nTelegram raqami: {user[4]}\nUnvoni: {user[6]}")
    else:
        await message.reply("Biror xabarni 'reply' qilib /about buyrug'ini kiriting:", reply_markup=menu_btn)



@dp.message_handler(text="/users", user_id=ADMINS)
async def get_all_users(message: types.Message):
    all_users = db.select_all_users()
    await message.answer(f"Bot foydalanuvchilari: {len(all_users)}")

@dp.message_handler(user_id=ADMINS, content_types=types.ContentType.ANY)
async def answer_message(message: types.Message):
    if message.reply_to_message:
        try:
            if message.reply_to_message.forward_sender_name:
                user = db.select_user(tg_name=message.reply_to_message.forward_sender_name)
            else:
                user = db.select_user(telegram_id=message.reply_to_message.forward_from.id)
            await bot.send_message(chat_id=user[1], text="Sizga javob keldi:")
            await message.send_copy(chat_id=user[1])
            await message.reply("Xabar yuborildi ✅")
        except Exception as err:
            pass
            # await message.reply(f"Xabar yuborilmadi: {err}")
            