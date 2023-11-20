from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_btn_ru = ReplyKeyboardMarkup(
    keyboard=[
        
        [
            KeyboardButton(text="📨 Сообщить о коррупции"),              
            ],
       
        [
            KeyboardButton(text="🇺🇿/🇷🇺 Настройка языка бота"),
            # KeyboardButton(text="Ma'lumotlarimni o'zgartirish"),
        ]
       
    ],
    resize_keyboard=True,
    input_field_placeholder="Главное меню"

)
menu_btn = ReplyKeyboardMarkup(
    keyboard=[
        
        [
            KeyboardButton(text="📨 Korrupsiya haqida xabar berish"),              
            ],
 
        [
            KeyboardButton(text="🇺🇿/🇷🇺 Bot tilini sozlash"),
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
