import sqlite3
import time
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot

from aiogram.dispatcher import FSMContext
from keyboards.default.defoult_btn import back_btn, menu_btn, message_phone


@dp.message_handler(text="/start")
async def start_bot(message: types.Message, state=FSMContext):
    pass
    
    