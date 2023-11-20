from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Asosiy menu
menu_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📆 Dars jadvali"),              
            ],
        [
            KeyboardButton(text="📄 Talaba xujjatlari"),              
            ],
        [
            KeyboardButton(text="📨 Dekanatga xabar yozish"),
        ]
       
    ],
    resize_keyboard=True,
    input_field_placeholder="Asosiy menu"

)


message_phone = ReplyKeyboardMarkup(
        keyboard=[
            
            [
                KeyboardButton(text="☎️ Phone number", request_contact=True),              
                ],
         
        ],
        resize_keyboard=True,
        input_field_placeholder="Phone number is required"

    )

back_btn = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🔙 Back"), 
                ],
        ],
        resize_keyboard=True,
        input_field_placeholder="Back to menu"

    )
