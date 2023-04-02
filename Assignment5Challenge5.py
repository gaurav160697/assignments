class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate) / 100
savings_account = SavingsAccount("John Doe", 5000, 5)
print(savings_account.getBalance())
savings_account.deposit(2000)
print(savings_account.getBalance())
savings_account.withdrawal(1000)
print(savings_account.getBalance())
print(savings_account.interestAmount())
