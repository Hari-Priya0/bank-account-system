class Account:
    def __init__(self, name, acc_number, balance=0):
        self.name = name
        self.acc_number = acc_number
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("❌ Amount must be greater than zero.")
            return
        self.__balance += amount
        print(f"{amount} deposited. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Amount must be greater than zero.")
            return
        if amount > self.__balance:
            print("❌ Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.__balance}")

    def display(self):
        print("\n----- Account Details -----")
        print(f"Name           : {self.name}")
        print(f"Account Number : {self.acc_number}")
        print(f"Balance        : {self.__balance}")

    def get_balance(self):
        return self.__balance

class SavingsAccount(Account):
    def withdraw(self, amount):
        print("Savings account withdrawal")
        super().withdraw(amount)

accounts = {}

def create_account():
    name = input("Enter your name: ")
    acc_number = input("Enter a new account number: ")
    if acc_number in accounts:
        print("❌ Account number already exists!")
        return
    acc_type = input("Enter account type (savings/general): ").lower()
    if acc_type == "savings":
        accounts[acc_number] = SavingsAccount(name, acc_number)
    else:
        accounts[acc_number] = Account(name, acc_number)
    print("✅ Account created successfully!")

def deposit_money():
    acc_number = input("Enter your account number: ")
    if acc_number in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_number].deposit(amount)
    else:
        print("❌ Account not found!")
        
def withdraw_money():
    acc_number = input("Enter your account number: ")
    if acc_number in accounts:
        amount = float(input("Enter amount to withdraw: "))
        accounts[acc_number].withdraw(amount)
    else:
        print("❌ Account not found!")

def display_account():
    acc_number = input("Enter your account number: ")
    if acc_number in accounts:
        accounts[acc_number].display()
    else:
        print("❌ Account not found.")

def check_balance():
    acc_number = input("Enter your account number: ")
    if acc_number in accounts:
        print(f"Available Balance: {accounts[acc_number].get_balance()}")
    else:
        print("❌ Account not found.")

def list_all_accounts():
    if not accounts:
        print("⚠️ No accounts found.")
        return
    print("\n📋 All Account Holders:")
    for acc_no, acc_obj in accounts.items():
        print(f"{acc_no} - {acc_obj.name}")

while True:
    print("\n===== 🏦 BANK MENU =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Account Details")
    print("5. Check Balance")
    print("6. List All Accounts")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        create_account()
    elif choice == '2':
        deposit_money()
    elif choice == '3':
        withdraw_money()
    elif choice == '4':
        display_account()
    elif choice == '5':
        check_balance()
    elif choice == '6':
        list_all_accounts()
    elif choice == '7':
        print("Thank you for using our bank system!")
        break
    else:
        print("⚠️ Invalid choice! Please try again.")
