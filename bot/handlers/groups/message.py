from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
from filters.group_chat import IsGroup

Group_id = -1001704364861 # new bot tester



# @dp.message_handler(chat_type=[types.ChatType.SUPERGROUP, types.ChatType.GROUP], content_types=types.ContentType.ANY)
# @dp.message_handler(user_id=2079362883, content_types=types.ContentType.ANY)
# async def answer_message(message: types.Message):
#     if message.reply_to_message:
#         try:
#             if message.reply_to_message.forward_sender_name:
#                 user = db.select_user(tg_name=message.reply_to_message.forward_sender_name)
#             else:
#                 user = db.select_user(telegram_id=message.reply_to_message.forward_from.id)
#             await bot.send_message(chat_id=user[1], text="Sizga javob keldi:")
#             await message.send_copy(chat_id=user[1])
#             await message.reply("Xabar yuborildi ✅")
#         except Exception as err:
#             pass
#             # await message.reply(f"Xabar yuborilmadi: {err}")