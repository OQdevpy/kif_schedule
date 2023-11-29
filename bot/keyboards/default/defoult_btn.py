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
        ],
        #  [
        #     KeyboardButton(text="📄 Dekanatga hujjat yuborish"),
        # ]
       
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


def student_documents_btn(docs):
    docs_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    for d in docs:
        docs_btn.insert(KeyboardButton(text=d['title']))

    docs_btn.add(KeyboardButton(text="🔙 Back"))

    return docs_btn