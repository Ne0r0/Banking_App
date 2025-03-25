from account import Account

class Bank:
    def __init__(self):
        self.__accounts = {}

    def create_account(self, email):
        account = Account(email)
        self.__accounts[email] = account
        return account
    
    def login(self, email, password):
        account = self.__accounts.get(email)
        if account and account.check_password(password):
            return account
        return None