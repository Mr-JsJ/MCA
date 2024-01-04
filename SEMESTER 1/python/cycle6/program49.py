class BankAccount:
    def __init__(self, name, account_number, account_type, initial_balance=0):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful.")
        else:
            print("Deposit amount should be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawal of ${amount} successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount should be greater than zero.")

    def display_details(self):
        print(f"Account Details\nName: {self.name}\nAccount Number: {self.account_number}\nAccount Type: {self.account_type}\nBalance: ${self.balance}")


name = input("Enter depositor's name: ")
account_number = input("Enter account number: ")
account_type = input("Enter account type: ")
initial_balance = float(input("Enter initial balance: "))

account = BankAccount(name, account_number, account_type, initial_balance)
account.display_details()

deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)

account.display_details()
