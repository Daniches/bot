from random import randrange, choice
from modules.base_module import BaseModule


class GeneratePassword(BaseModule):
    def __init__(self):
        pass

    def run(self, update, context):
        symbols='1234567890-=qwertyuiopasdfghjklzxcvbnm,./!^&*()_+QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?`~[]'
        l = randrange(8, 16)
        password_ = ""
        for t in range(l):
            password_ += choice(symbols)

        self.send(update, context, "Это твой пароль: " + password_ + "\nНикому не сообщай его!")


generate_password_module = GeneratePassword()