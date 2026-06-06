# Day3的 5 个练习：
'''
# 用 for 循环打印 1 到 20 的所有奇数
for num in range(1,20,2):
    print(num)

# 用 while 循环计算 1+2+3+...+100 的和，打印结果
n = 1
total = 0
while n < 101:
    total += n
    n += 1
print(sum)

# 用 for 循环遍历字符串 "hello"，逐个打印每个字母
for i in "Hello":
    print(i)

# 用 for + break：在列表 [3, 7, 2, 9, 4, 6] 里找到第一个大于 5 的数，打印它然后停止
L = [3, 7, 2, 9, 4, 6]
for index, num in enumerate(L):
    if num > 5:
        print(f'The first num > 5 is {num}, in the position of {index}.')
        break


# 用 for + continue：打印 1 到 15 中所有不能被 3 整除的数
for i in range(1,16):
    
    if i % 3 == 0:
        continue
    
    print(i)
 '''       




# Day 4 任务：综合练习，写 3 个小程序

# 温度转换（摄氏度 ↔ 华氏度，用户输入选择转换方向）
raw_temp = float(input('Input the degree you want to transger: '))
direction = input('Input the direction you want to transfer:"C to F" or "F to C" ')
direc_temp = 0

if direction == "C to F":
    direc_temp = raw_temp * 9 / 5 + 32
    print(f"Fahrenheit Degree is {direc_temp:.2f}.")

elif direction == "F to C":
    direc_temp = (raw_temp - 32) * 5 / 9
    print(f"Celsius Degree is {direc_temp:.2f}.")

else:
    print("Invaild Input!")


# BMI 计算（输入身高体重，输出 BMI 值和分类）
weight = float(input("Weight(kg): "))
height = float(input("Height(m)"))

bmi = weight / height**2

if bmi < 18.5:
    print(f"BMI: {bmi:.2f}. A little thin.")
elif bmi < 23.9:
    print(f"BMI: {bmi:.2f}. Normal.")
elif bmi < 27.9:
    print(f"BMI: {bmi:.2f}. Overweight.")
elif bmi >= 27.9:
    print(f"BMI: {bmi:.2f}. Fat.")
else:
    print("Invaild.")


#猜数字游戏（程序随机生成 1-100 的数，用户猜，给出大了/小了的提示，猜对结束）
import random

number = random.randint(1, 100)

while True:
    guess_num = int(input("Input an integer number in [1,100] you guess: "))
    if guess_num == number:
        print("Win!")
        break

    elif guess_num > number:
        print("Too Large.")
    
    elif guess_num < number:
        print("Too Small.")
