class BankAccount:
    def __init__(self, name, balance=0):   # constructor
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance


# Example usage with input:
name = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(name, initial_balance)

# Deposit
deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)

# Withdraw
withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)

# Check balance
account.check_balance()


