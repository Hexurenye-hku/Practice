'''
#第 3 题：输入一个整数，判断它是奇数还是偶数，打印结果。
input_num = input("Input an integer: ")
input_num = int(input_num)

if input_num %2 == 0:
    print("偶数")
else:
    print("奇数")

'''
5

#第 4 题：输入三个数 a、b、c，找出最大的那个，打印出来。
a = input("Input a: ")
b = input("Input b: ")      
c = input("Input c: ")  
a = int(a)
b = int(b)  
c = int(c)

if a > b and a > c:
    print("最大数是：", a)
elif b > a and b > c:
    print("最大数是：", b)
elif c > a and c > b:
    print("最大数是：", c)    
else:
    print("输入的数有重复，无法判断最大数")




'''
#第 5 题：输入一个年份，判断是否是闰年。闰年规则自己查（这也是本周末的作业题，提前练）。
year = input("Input a year: ")
year = int(year)

if (year % 4 == 0 and year %100 !=0) or (year % 400 == 0):
    print(year, "是闰年")
else:
    print(year, "不是闰年")

'''