class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = initial_balance
            print(f"Account {account_number} created with initial balance ${initial_balance:.2f}.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"${amount:.2f} deposited into account {account_number}.")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"${amount:.2f} withdrawn from account {account_number}.")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Account balance for account {account_number}: ${self.accounts[account_number]:.2f}.")
        else:
            print("Account not found.")

bank = Bank()

bank.create_account("123456", 1000)
bank.create_account("789012", 500)

bank.deposit("123456", 500)

bank.withdraw("789012", 200)

bank.check_balance("123456")
bank.check_balance("789012")