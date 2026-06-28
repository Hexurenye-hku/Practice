'''
练习:用继承改造 BankAccount
基于你已有的 BankAccount(私有属性版),写两个子类:
子类 1:SavingsAccount(储蓄账户)

继承 BankAccount
新增一个方法 add_interest(rate):按当前余额乘以利率 rate,把利息存入账户。比如余额 1000、rate 0.05,就给账户加 50
难点:余额是私有属性 __balance,在子类里你直接访问不到 self.__balance(name mangling 会让它变成 _SavingsAccount__balance,指岔了)。想想:你怎么在子类里给账户加钱?(提示:父类有现成的方法可以用)

子类 2:CreditAccount(信用账户)

继承 BankAccount
初始化时多接收一个参数 limit(信用额度,比如 500),表示余额最低可以到 -limit
重写(override) withdraw 方法:允许透支,只要取款后余额不低于 -limit 就准取
难点:子类的 __init__ 要既接收父类的 owner/balance,又接收自己新增的 limit。这需要在子类 __init__ 里调用父类的 __init__ 来处理 owner 和 balance。这个语法你查一下——关键词 super()。

两个难点我都只给了方向(父类方法、super()),具体怎么写自己查文档 + 试。super() 是今天的新语法,查不到再问我,但先自己查。
写完贴代码 + 测试(测试要验证:储蓄账户加利息正确;信用账户能透支到额度、但超过额度被拒)。
这道题有分量,慢慢写,卡住先自己想,真卡死再来。
'''

from p1_w2_d2_accon import BankAccount

class SavingAccount(BankAccount):
    def add_interest(self,rate):
        interest = rate * self.get_balance()
        self.deposit(interest)
        return True

class CreditAccount(BankAccount):
    def __init__(self, owner, balance=0, limit = 500):
        super().__init__(owner, balance)
        self.limit = limit
    
    def withdraw(self, amount):
        if self.get_balance() + self.limit >= amount :
            self.deposit(-amount)
            return True
    
        else:
            print("Balance is not enough")
            return False     

    def show_balance(self):
        if self.get_balance() >= 0:
            return super().show_balance() 
        else:
            return super().show_balance() + f'(Overdraft In Progress: {abs(self.get_balance())} of the credit limit already used.)'
        
'''
sa_test = SavingAccount('Bruce', 1000)
sa_test.add_interest(0.05)
print(sa_test.show_balance())
'''

ca_test = CreditAccount('Hanwen', 100, 500)

print(ca_test.show_balance())

ca_test.withdraw(300)
print(ca_test.show_balance())

ca_test.withdraw(200)
print(ca_test.show_balance())

ca_test.withdraw(100)
print(ca_test.show_balance())