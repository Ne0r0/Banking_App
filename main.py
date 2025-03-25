from bank import Bank
from logger import log_action

def main():
    bank = Bank()

    while True:
        print("Bank Application")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            email = input("Enter your email: ")
            account = bank.create_account(email)
            log_action(f"Account created: ID={account.get_id()}, Email={email}")
            print(f"Account has been created. Your ID: {account.get_id()}")
            print(f"Your generated password: {account.get_password()}")
            print("Please save your password securely.")
        
        elif choice == '2':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            account = bank.login(email, password)
            if account:
                log_action(f"Successful login: Email={email}")
                print(f"Login successful! Welcome, {account.get_email()}")
            else:
                log_action(f"Failed login attempt: Email={email}")
                print("Invalid email or password.")

        elif choice == '3':
            print("See you later")
            break
        else:
            print("Please choose from the options listed")

if __name__ == "__main__":
    main()
