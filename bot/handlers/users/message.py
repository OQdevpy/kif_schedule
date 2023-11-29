from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from keyboards.default.defoult_btn import message_phone, back_btn, menu_btn
from loader import dp, bot
from data.api import get_user_by_id, update_full_name, update_phone, update_user_full_name, update_tg_username

@dp.message_handler(text = '📨 Dekanatga xabar yozish')
async def message_write(message: types.Message, state: FSMContext):
    user = get_user_by_id(tg_id=message.from_user.id)
    print(user)
    print("============================================")
    if not user.get("phone_number"):
        await message.answer("Ism Familiyangizni yuboring", reply_markup=back_btn)
        await state.set_state("full_name")
    else:
        await message.answer(f"Dekanatga yubormoqchi bo'lgan xabaringizni yuboring (rasm, video, audio, matn)", reply_markup=types.ReplyKeyboardRemove())
        await state.set_state("message")


@dp.message_handler(state="full_name", text ="🔙 Back")
async def input_password(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"Asosiy sahifa", reply_markup=menu_btn)
    

@dp.message_handler(state="full_name")
async def get_full_name(message: types.Message, state: FSMContext):
    full_name = message.text
    await state.update_data(full_name=full_name)
    await message.answer(f"Telefon raqamingizni yuboring", reply_markup=message_phone)
    await state.set_state("phone")
    

@dp.message_handler(state="phone", text ="🔙 Back")
async def input_password(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"Asosiy sahifa", reply_markup=menu_btn)
    

@dp.message_handler(state="phone", content_types=types.ContentType.CONTACT)
async def get_phone(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number   
    data = await state.get_data()
    user_name = data['full_name']
    user_id = message.from_user.id
    if message.from_user.username:
        username = message.from_user.username
    else:
        username = ""
    update_phone(telegram_id=user_id, phone=phone)
    update_user_full_name(telegram_id=user_id, full_name=user_name)
    update_full_name(telegram_id=user_id, full_name=message.from_user.full_name)
    update_tg_username(telegram_id=user_id, username=username)
    
    await message.answer(f"Dekanatga yubormoqchi bo'lgan xabaringizni yuboring (rasm, video, audio, matn): ", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state("message")

@dp.message_handler(state="phone")
async def get_phone(message: types.Message, state: FSMContext):
    await message.answer("Quidagi tugma yordamida telefon raqamingizni yuboring👇", reply_markup=message_phone)
    await state.set_state("phone")
    


@dp.message_handler(state="message", content_types=types.ContentType.ANY)
async def send_message(message: types.Message, state: FSMContext):
    user_ = message.from_user
    await message.forward(chat_id=-1001795943163, message_thread_id=2)
    update_full_name(telegram_id=user_.id, full_name=user_.full_name)
    await message.answer(f"Xabaringiz yuborildi ✅", reply_markup=menu_btn)
    await state.finish()
