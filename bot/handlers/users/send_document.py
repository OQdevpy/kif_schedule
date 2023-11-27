from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from keyboards.default.defoult_btn import menu_btn
from loader import dp, bot
from data.api import update_full_name,  update_tg_username

@dp.message_handler(text = '📄 Dekanatga hujjat yuborish')
async def message_write(message: types.Message, state: FSMContext):

    user_id = message.from_user.id
    if message.from_user.username:
        username = message.from_user.username
    else:
        username = ""
    update_full_name(telegram_id=user_id, full_name=message.from_user.full_name)
    update_tg_username(telegram_id=user_id, username=username)
    
    await message.answer(f"Dekanatga yubormoqchi bo'lgan hujjatingiz haqida to'liq ma'lumotingizni kiriting va hujjatingiz bilan birga 1 ta xabarda yuboring", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state("send_document")


@dp.message_handler(state="send_document", content_types=types.ContentType.ANY)
async def send_message(message: types.Message, state: FSMContext):
    await message.forward(chat_id=-1001795943163, message_thread_id=4)
    await message.answer(f"Xabaringiz yuborildi ✅", reply_markup=menu_btn)
    await state.finish()
