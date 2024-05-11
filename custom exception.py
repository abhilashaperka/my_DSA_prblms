class InSufficientBalance(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"insufficient balance: Available balance is {balance} but need {amount}")

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def withdraw(self, amount):
        if self.balance < amount:
            raise InSufficientBalance(self.balance, amount)
        self.balance -= amount
        print(f"Withdrawal of {amount} successful. Updated bank balance: {self.balance}")

try:
    account = BankAccount("1234567890", 50000)
    account.withdraw(70000)
except InSufficientBalance as e:
    print("Error:", e)
 
                         