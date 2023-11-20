from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from keyboards.default.defoult_btn import message_phone, back_btn, menu_btn, menu_btn_ru
from loader import dp, db, bot


@dp.message_handler(text = '📨 Dekanatga xabar yozish')
async def message_write(message: types.Message, state: FSMContext):
    # user = db.select_user(telegram_id=message.from_user.id)
    user = [1,2,2,3,0]
    txt  = """
        Murojaatingiz avvalida Universitetga aloqangiz ya'ni professor-o'qituvchi, xodim, talaba, ota-ona, boshqa shaxs fakultet, kurs, familiya ismingiz, telefon raqamingiz to'g'risidagi ma'lumotlarni kiritishingiz mumkin.

        Murojaatchi shaxsi sir saqlanishi kafolatlanadi.    
"""
    if not user[4]:
        await message.answer(txt)
        await message.answer("Ism Familiyangizni yuboring", reply_markup=back_btn)
        await state.set_state("full_name")
    else:
        await message.answer(f"Dekanatga yubormoqchi bo'lgan xabaringizni yuboring (rasm, video, audio, matn)", reply_markup=types.ReplyKeyboardRemove())
        await state.set_state("message")


@dp.message_handler(state="full_name", text ="🔙 Back")
async def input_password(message: types.Message, state: FSMContext):
    user_id = message.from_user.id   
    await state.finish()
    await message.answer(f"Asosiy sahifa",reply_markup=menu_btn)
    

@dp.message_handler(state="full_name")
async def get_full_name(message: types.Message, state: FSMContext):
    text = """ Murojaatingiz avvalida Universitetga aloqangiz ya'ni professor-o'qituvchi, xodim, talaba, ota-ona, boshqa shaxs fakultet, kursingiz to'g'risidagi ma'lumotlarni kiritishingiz mumkin."""
    full_name = message.text
    await state.update_data(full_name=full_name)
    await message.answer(text)
    await state.set_state("unvon")
    

    
@dp.message_handler(state="unvon")
async def get_full_name(message: types.Message, state: FSMContext):
    unvon = message.text
    await state.update_data(unvon=unvon)
    await message.answer(f"Telefon raqamingizni yuboring", reply_markup=message_phone)
    await state.set_state("phone")
    

@dp.message_handler(state="phone", text ="🔙 Back")
async def input_password(message: types.Message, state: FSMContext):
    user_id = message.from_user.id   
    await state.finish()
    await message.answer(f"Asosiy sahifa",reply_markup=menu_btn)
    

@dp.message_handler(state="phone", content_types=types.ContentType.CONTACT)
async def get_phone(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number   
    data = await state.get_data()
    full_name = data['full_name']
    unvon = data['unvon']
    if message.from_user.username:
        username = message.from_user.username
    else:
        username = ""
    # db.update_user_data(telegram_id=message.from_user.id, full_name=full_name, user_name=username, phone_num=phone, unvon=unvon)
  
    
    await message.answer(f"Dekanatga yubormoqchi bo'lgan xabaringizni yuboring (rasm, video, audio, matn): ", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state("message")

@dp.message_handler(state="phone")
async def get_phone(message: types.Message, state: FSMContext):
    await message.answer("Quidagi tugma yordamida telefon raqamingizni yuboring👇", reply_markup=message_phone)
    await state.set_state("phone")
    


@dp.message_handler(state="message", content_types=types.ContentType.ANY)
async def send_message(message: types.Message, state: FSMContext):

    await message.forward(chat_id=973108256)
    # await message.forward(chat_id=2079362883)
    # db.update_tg_name(telegram_id=message.from_user.id, tg_name=message.from_user.full_name)
    await message.answer(f"Xabaringiz yuborildi ✅", reply_markup=menu_btn)

    await state.finish()