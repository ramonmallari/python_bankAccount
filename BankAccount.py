class BankAccount:
    def __init__(self, int_rate, balance):
        self.rate = int_rate
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        after_withdrawal = self.balance - amount
        if self.balance < 0:
            print("Insufficient funds: $5 dollar fee.")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}, Interest Rate: {self.rate}")
    def yield_interest(self):
        if self.balance > 0:
            self.interest_yield = self.balance * self.rate
            self.balance += interest_yield
        return self
account_one = BankAccount(.24,0)
account_two = BankAccount(.15,0)
#print(account_one.rate)
#print(account_two.rate)
account_one.deposit(1200).deposit(5000).deposit(250).withdraw(325).display_account_info()
account_two.deposit(2000).deposit(915).withdraw(25).withdraw(60).withdraw(50).withdraw(35).display_account_info()


