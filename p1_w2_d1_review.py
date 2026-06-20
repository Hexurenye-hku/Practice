class BankAccount(object):
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            return "Balance is not enough"
    
    def show_balance(self):
        return f"{self.owner}'s account balance is {self.balance}."