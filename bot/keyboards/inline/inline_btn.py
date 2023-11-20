from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

lang_btn = InlineKeyboardMarkup(
	inline_keyboard=[
	[
		InlineKeyboardButton(text="🇺🇿 Uzbek", callback_data="uzbek"),
		InlineKeyboardButton(text="🇷🇺 Russian", callback_data="russian"),
	],
])

