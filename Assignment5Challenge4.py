class Account:
    def __init__(self, title, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

account = Account("Ashish", 5000)
print(account.title)
print(account.balance)

savingsAccount = SavingsAccount("Ashish", 5000, 5)
print(savingsAccount.title)
print(savingsAccount.balance)
print(savingsAccount.interestRate)
