from aiogram import types
from data.config import ADMINS


from loader import dp, db, bot

from keyboards.default.defoult_btn import menu_btn


# get forward message 
# @dp.message_handler(content_types=types.ContentType.ANY, state='*')
# async def bot_echo(message: types.Message):
#     await message.forward(chat_id="-1001704364861" )
#     print(message)
    # if message.forward_from:
    #     print(message)
    #     print(message.forward_from)
    #     print(message.forward_from.id)
        
    #     await message.answer(message)
    
# Echo bot
@dp.message_handler( user_id=ADMINS)
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    await message.answer(message.text, reply_markup=menu_btn)
    
    
@dp.message_handler()
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    await message.answer(message.text, reply_markup=menu_btn)

    
    # chat = await bot.get_chat('@new_bot_test_group')
    # #    user = await bot.get_chat_member(chat_id="@new_bot_test_group", user_id=message.from_user.id)
    # isuser = await bot.get_chat_member(chat_id="-1001704364861", user_id=message.from_user.id) #status owner, administrator, member
    # # invite_link = await chat.export_invite_link()
    # # invite_link = chat['invite_link']
    # # print(chat)
    # # await message.answer(isuser)
    # # status = await bot.get_chat_member("-1001704364861", message.from_user.id)
    # # member_count = await bot.get_chat_member_count(chat_id=chat.id) ## member count
    
    
    # await message.answer(message.text)
    # if status['status'] == 'left':
    #     channel_info = [invite_link, chat.title, 0]
    # else:
    #     channel_info = [invite_link, chat.title, 1]
    #             aa += 1
    #         join_channel.append(cha
    # user_id = message.from_user.id
    # await message.answer(message.text, reply_markup=login_menu(user=IsTiftUser(user_id)))

