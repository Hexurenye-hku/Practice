# 练习 1：写函数 greet(name, age)，返回 "你好，我叫 xxx，今年 xx 岁。"
def greet(name, age):
    
    return f"你好，我叫{name}, 今年{age}岁。"

#print(greet('马走日', 18))

# 练习 2：写函数 format_price(price)，把数字格式化成保留两位小数的字符串，比如 3.5 → "3.50"
def format_price(price):

    return f"{price:.2f}"

# print(format_price(3.5))

# 练习 3：写函数 format_percent(score, total)，返回百分比字符串，比如 23, 50 → "46.00%"
def format_percent(score, total):

    return f"{ score / total :.2%}"

# print(format_percent(23, 50))

# 练习 4：写函数 pad_number(n)，把数字格式化成 5 位宽度、不足补零，比如 42 → "00042"
def pad_number(n):
    
    return f"{n:0>5}"

# print(pad_number(42))

# 练习 5：写函数 summary(name, score, rank)，返回 "姓名：xxx | 分数：xx.xx | 排名：第 x 名"
def summary(name, score, rank):

    return f"姓名：{name.capitalize()} | 分数：{score:.2f} | 排名：第{rank}名"

# print(summary('bruce', 98.2, 2))