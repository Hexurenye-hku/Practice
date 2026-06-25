class BankAccount(object):
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            # print("Balance is not enough")
            return False
    
    def show_balance(self):
        return f"{self.owner}'s account balance is {self.balance}."

    def transfer(self, other, amount):
        if self.withdraw(amount):
            other.deposit(amount)
            print("Transfer Success")
            return True
        else:
            print('Balance is not enough')
            return False
            

a = BankAccount('张三', 100)   # 注意,这次张三只有 100
b = BankAccount('李四', 500)
a.transfer(b, 300)             # 张三想转 300,但他只有 100
print(a.show_balance())
print(b.show_balance())