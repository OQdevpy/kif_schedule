from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp,  bot


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish\n",
            "/help - Yordam\n",
            )
    
    await message.answer("\n".join(text))
    
# @dp.message_handler(content_types=types.ContentType.ANY)
# async def print(message: types.Message):
#     await message.answer(message.animation.file_id)
#     await message.answer_animation(animation="CgACAgIAAxkBAAIBVmUrom5MlQGUprxFX05vPLDTv2K0AAIjNwACWF9gSff17npwgdPWMAQ", caption="Xatolik yuz berdi")