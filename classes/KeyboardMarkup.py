from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class KeyboardMarkup:
    def __init__(self, buttons, big=True, placeholder=""):
        btns = []

        for button_text in buttons:
            btns.append(KeyboardButton(text=button_text))

        self.inst = ReplyKeyboardMarkup(
            keyboard=btns, resize_keyboard=big, input_field_placeholder=placeholder
        )


'''
main2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Тестова кнопка 1", callback_data="test-0"),
     InlineKeyboardButton(text="Тестова кнопка 2", callback_data="test-1")],
    [InlineKeyboardButton(text="Тестова кнопка 3", callback_data="test-2")
     ]])

'''
