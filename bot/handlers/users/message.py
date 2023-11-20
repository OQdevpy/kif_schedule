from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from keyboards.default.defoult_btn import message_phone, back_btn, menu_btn, menu_btn_ru
from loader import dp, db, bot


@dp.message_handler(text = '📨 Korrupsiya haqida xabar berish')
async def message_write(message: types.Message, state: FSMContext):
    user = db.select_user(telegram_id=message.from_user.id)
    txt  = """
Murojaatingiz avvalida Universitetga aloqangiz ya'ni professor-o'qituvchi, xodim, talaba, ota-ona, boshqa shaxs fakultet, kurs, familiya ismingiz, telefon raqamingiz to'g'risidagi ma'lumotlarni kiritishingiz mumkin.

Murojaatchi shaxsi sir saqlanishi kafolatlanadi.
"""
    if not user[4]:
        await message.answer(txt)
        await message.answer("Ism Familiyangizni yuboring", reply_markup=back_btn)
        await state.set_state("full_name")
    else:
        await message.answer(f"Korrupsiyaga doir qandaydir xolatga duch kelgan bo'lsangiz, bizga uni matn, audio, rasm yoki video ko'rinishida yuboring yuboring:", reply_markup=types.ReplyKeyboardRemove())
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
    db.update_user_data(telegram_id=message.from_user.id, full_name=full_name, user_name=username, phone_num=phone, unvon=unvon)
  
    
    await message.answer(f"Korrupsiyaga doir qandaydir xolatga dush kelgan bo'lsangiz, bizga uni matn, audio, rasm yoki video ko'rinishida yuboring yuboring:", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state("message")

@dp.message_handler(state="phone")
async def get_phone(message: types.Message, state: FSMContext):
    await message.answer("Quidagi tugma yordamida telefon raqamingizni yuboring👇", reply_markup=message_phone)
    await state.set_state("phone")
    


@dp.message_handler(state="message", content_types=types.ContentType.ANY)
async def send_message(message: types.Message, state: FSMContext):

    await message.forward(chat_id=1201104723)
    # await message.forward(chat_id=2079362883)
    db.update_tg_name(telegram_id=message.from_user.id, tg_name=message.from_user.full_name)
    await message.answer(f"Xabaringiz yuborildi ✅", reply_markup=menu_btn)
    txt = """
Hurmatli murojaatchi, Sizning Universiteda korrupsion holatlarni oldini olishda qo’shgan hissangizni yuksak baholaymiz va sizga minnatdorchilik bildiramiz. 
"""
    await message.answer(txt)
    await state.finish()
    
    
    
    
    
    
@dp.message_handler(text="📨 Сообщить о коррупции")
async def message_write(message: types.Message, state: FSMContext):
    user = db.select_user(telegram_id=message.from_user.id)
    txt = """
Вы можете ввести информацию о себе, такую ​​как ваша фамилия, имя, номер телефона, должность, факультет, курс и т. Д., Связанные с университетом.

Личность жалобщика гарантируется.
"""
    if not user[4]:
        await message.answer(txt)
        await message.answer("Введите ваше имя и фамилию", reply_markup=back_btn)
        await state.set_state("full_name_ru")
    else:
        await message.answer(f"Если вы столкнулись с какой-либо коррупцией, отправьте нам ее в виде текста, аудио, фото или видео:", reply_markup=types.ReplyKeyboardRemove())
        await state.set_state("message_ru")
        
        
@dp.message_handler(state="full_name_ru", text ="🔙 Back")
async def input_password(message: types.Message, state: FSMContext):
    user_id = message.from_user.id   
    await state.finish()
    await message.answer(f"Главное меню",reply_markup=menu_btn_ru)
    
    
@dp.message_handler(state="full_name_ru")
async def get_full_name(message: types.Message, state: FSMContext):
    text = """ Вы можете ввести информацию о себе, такую ​​как ваша фамилия, имя, номер телефона, должность, факультет, курс и т. Д., Связанные с университетом."""
    full_name = message.text
    await state.update_data(full_name=full_name)
    await message.answer(text)
    await state.set_state("unvon_ru")
    
    
@dp.message_handler(state="unvon_ru")
async def get_full_name(message: types.Message, state: FSMContext):
    unvon = message.text
    await state.update_data(unvon=unvon)
    await message.answer(f"Введите ваш номер телефона", reply_markup=message_phone)
    await state.set_state("phone_ru")
    
    
@dp.message_handler(state="phone_ru", text ="🔙 Back")
async def input_password(message: types.Message, state: FSMContext):
    user_id = message.from_user.id   
    await state.finish()
    await message.answer(f"Главное меню",reply_markup=menu_btn_ru)
    
    
@dp.message_handler(state="phone_ru", content_types=types.ContentType.CONTACT)
async def get_phone(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number   
    data = await state.get_data()
    full_name = data['full_name']
    unvon = data['unvon']
    if message.from_user.username:
        username = message.from_user.username
    else:
        username = ""
    db.update_user_data(telegram_id=message.from_user.id, full_name=full_name, user_name=username, phone_num=phone, unvon=unvon)
  
    
    await message.answer(f"Если вы столкнулись с какой-либо коррупцией, отправьте нам ее в виде текста, аудио, фото или видео:", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state("message_ru")
    
    
@dp.message_handler(state="phone_ru")
async def get_phone(message: types.Message, state: FSMContext):
    await message.answer("Введите ваш номер телефона с помощью кнопки ниже👇", reply_markup=message_phone)
    await state.set_state("phone_ru")
    
    
@dp.message_handler(state="message_ru", content_types=types.ContentType.ANY)
async def send_message(message: types.Message, state: FSMContext):

    await message.forward(chat_id=1201104723)
    # await message.forward(chat_id=2079362883)
    db.update_tg_name(telegram_id=message.from_user.id, tg_name=message.from_user.full_name)
    await message.answer(f"Ваше сообщение отправлено ✅", reply_markup=menu_btn_ru)
    txt = """
Уважаемый заявитель, мы высоко ценим ваш вклад в борьбе с коррупцией в университете и благодарим вас.
"""
    await message.answer(txt)
    await state.finish()
    
    
    