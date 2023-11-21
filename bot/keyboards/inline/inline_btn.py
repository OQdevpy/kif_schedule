from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData



def schedule_kurs_btn_func(courses):
    schedule_kurs_btn = InlineKeyboardMarkup(row_width=2)

    for c in courses:
        schedule_kurs_btn.insert(InlineKeyboardButton(text=c['title'], callback_data=c['id']))

    return schedule_kurs_btn


def schedule_group_btn_func(groups):
    schedule_group_btn = InlineKeyboardMarkup(row_width=2)
    for g in groups:
        schedule_group_btn.insert(InlineKeyboardButton(text=g['title'], callback_data=g['id']))
    schedule_group_btn.add(InlineKeyboardButton(text="🔙 Back", callback_data="back")
    return schedule_group_btn