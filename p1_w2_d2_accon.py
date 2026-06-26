class BankAccount(object):
    def __init__(self, owner, balance = 0):
        self.__owner = owner
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        else:
            # print("Balance is not enough")
            return False
    
    def show_balance(self):
        return f"{self.__owner}'s account balance is {self.__balance}."
    
    def get_balance(self):
        return self.__balance

    def transfer(self, other, amount):
        if self.withdraw(amount):
            other.deposit(amount)
            print("Transfer Success")
            return True
        else:
            print('Balance is not enough')
            return False
            
'''
a = BankAccount('张三', 100)   
a.__balance = 99999999         
print(a.show_balance())
print(a.__balance)                    # 99999999 —— 你新建的垃圾属性
print(a._BankAccount__balance)        # 100 —— 真正的余额,没被动
'''