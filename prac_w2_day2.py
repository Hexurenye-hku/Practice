# Ex6.3
def mul(*nums):
    if not nums:
        raise TypeError("Empty Tuple.")
    
    product = 1

    for i in nums:
        product = product * i
    
    return product

# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')

# Ex1:
def greet(name, greeting = 'Hello'):
    print(f"{greeting}, {name}!")

# test
greet('Dingzhen')
greet('Liujianlong','你好')
greet(1)
try:
    greet()
    
except TypeError:
    print("Error")

# Ex2:
def sum_all(*nums):
    if not nums:
        raise TypeError("Empty.")
    
    n = 0
    for i in nums:
        n += i
    
    return n

# test
print(sum_all(1,2,3,4,5,6))
print(sum_all(123124))
print(sum_all())


# Ex3
def describe(**info):
    if not info:
        raise TypeError("NULL")
    
    for i in info:
        print(f"{i}:{info[i]}") 

# test
t_info = {'city':'hk', 'school':'hku', 'department':'geography'}
describe(**t_info)
describe(a=1, b=2, c=3)
describe()

# Ex 4 power(base, exp=2)：计算 base 的 exp 次方（不许用 ** 运算符，用循环） 默认参数 + 循环逻辑
def power(base, exp = 2):
    if exp == 0:
        return 1
    
    n = base
    times = exp
    while times > 1:
        n = n * base
        times -= 1

    return n
# test
print(power(2))
print(power(2,3))
print(power(5,0))
print(power(3,1))


# Ex 5 mix(a, b, *args, sep="-")：把 a、b 和所有 args 用 sep 连接成字符串返回 混合参数
def mix(a, b, *args, sep = "-"):
    
    final = str(a) + sep + str(b)

    for i in args:
        last_str = sep + str(i)
        final = final + last_str
    
    return final

# test
print(mix(1, 2))
print(mix(1, 2, 3, 4))
print(mix(1, 2, 3, sep="+"))
