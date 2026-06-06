year = int(input("Is this year a leap year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("True")

else:
    print("False")


year = int(input("Is this year a leap year: "))

def is_leap_year(year):
    if not isinstance(year, int): #  isinstance 检查在这个用法里永远不会触发。因为 int(input(...)) 已经把输入强制转成 int 了——如果用户输入"abc"，int() 自己就先崩了，根本到不了你的函数。
        raise TypeError("Invalid Input. Only integer allowed.") # 防御写在了错误的地方

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

print(f"{year} is leap: ", is_leap_year(year))