# 练习 1：写函数 make_profile(name, age, city)，返回一个包含这三个键的字典
def make_profile(name, age, city):
    return {'name' : name, 'age' : age, 'city' : city}

# print(make_profile('Bruce', 25, 'HongKong'))

# 练习 2：写函数 add_score(d, subject, score)，往字典 d 里加入一个科目和分数，返回更新后的字典
def add_score(d, subject, score):
    d[subject] = score
    return d
d1 = {'7307' : 'A-', '7303' : 'B+', '7305' : 'A'}
# print(add_score(d1, '7306','A'))

# 练习 3：写函数 get_grade(d, subject)，从字典里取某科分数，如果该科不存在返回 "未找到"
def get_grade(d, subject):
    return d.get(subject, "未找到")
    
# print(get_grade(d1, '7307'))
# print(get_grade(d1, '7306'))

# 练习 4：写函数 remove_subject(d, subject)，删除字典里某个科目，如果不存在就什么都不做，返回更新后的字典
def remove_subject(d, subject):
    d.pop(subject, None)
    return d

# print(remove_subject(d1, '7307'))
# print(remove_subject(d1, '7306'))

# 练习 5：写函数 print_profile(d)，遍历字典，每行打印 "key: value" 的格式
def print_profile(d):
    for k, v in d.items():
        print(f"{k}: {v}")
print_profile(d1) 
