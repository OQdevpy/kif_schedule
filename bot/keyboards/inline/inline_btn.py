from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData



def schedule_kurs_btn_func(courses=4):
    schedule_kurs_btn = InlineKeyboardMarkup(row_width=2)

    for c in range(1, courses+1):
        schedule_kurs_btn.insert(InlineKeyboardButton(text=f"{c} - kurs", callback_data=f"course_{c}"))

    return schedule_kurs_btn


def schedule_group_btn_func(groups):
    schedule_group_btn = InlineKeyboardMarkup(row_width=2)
    for g in groups:
        schedule_group_btn.insert(InlineKeyboardButton(text=g['academic_code'], callback_data=f"group_{g['id']}"))
    schedule_group_btn.add(InlineKeyboardButton(text="🔙 Back", callback_data="back"))
    return schedule_group_btn