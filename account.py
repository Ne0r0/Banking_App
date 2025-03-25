import random
import string

class Account:
    def __init__(self, email):
        self.__id = random.randint(1000, 9999)
        self.__email = email
        self.__password = self.__generate_password()

    def __generate_password(self, length=10):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def get_id(self):
        return self.__id
    
    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password
    
    def check_password(self, password):
        return self.__password == password