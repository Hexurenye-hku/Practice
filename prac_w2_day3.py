# 题1：写函数 remove_duplicates(lst)，输入一个列表，返回去掉重复元素后的新列表，且保持原来的顺序。
# 例：[3, 1, 2, 1, 3] → [3, 1, 2]
def remove_duplicates(lst):
    new_lst = []

    for i in lst:
        if i not in new_lst:
            new_lst.append(i)

    return new_lst


# 题2：写函数 flatten(nested)，输入一个二维列表（列表里面套列表），返回一个一维列表。
# 例：[[1,2],[3,4],[5]] → [1,2,3,4,5]
def flatten(nested):
    new_lst = []

    for i in nested:
        for j in i:
            new_lst.append(j)
    
    return new_lst


# 题3：写函数 top_n(lst, n)，返回列表中最大的 n 个数，从大到小排列，不能用 sorted() 或 sort()。
# 例：top_n([3,1,4,1,5,9,2,6], 3) → [9,6,5]
def top_n(lst, n):
    lst = lst[:] #函数默认不应该修改传入的参数，第一行先 lst = lst[:] 复制一份再操作。
    new_lst = []

    for j in range(0, n):
        max_num = lst[0]
        for i in lst:
            if max_num >= i:
                continue
            else:
                max_num = i
        
        new_lst.append(max_num)
        lst.remove(max_num)
    
    return new_lst

# Ex 6.4
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
# 然后打印出把所有盘子从A借助B移动到C的方法

def move(n, a, b, c): # n是盘子数，a是起点，b是中转，c是终点。
    
    if n == 1:
        return print(a, '-->', c)

    move(n-1,a, c, b) # n-1是盘子数，a是起点，c是中转，b是终点。这步是把n-1个盘子从A移到B，借助C

    print(a, "-->", c) # 打印：最大盘从A移到C

    move(n-1, b, a, c) #n-1个盘子从B移到C，借助A


# 递归练习2：写函数 sum_digits(n)，输入一个正整数，返回各位数字之和。
# 例：sum_digits(1234) → 10
# 要求：用递归实现，不能用循环，不能把数字转成字符串。

def sum_digits(n):

    if n // 10 == 0:
        return n

    return n % 10 + sum_digits(n // 10) 


# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
    if not s:
        return''
    
    count_spa = 0

    for i in s:
        if i != ' ':
            start = s.index(i)
            break

        else:
            count_spa += 1

        if count_spa == len(s):
            return''

    j = len(s) - 1
    while j > 0:
        if s[j] != ' ':
            end = j
            break      
        j -= 1



    return s[start:end+1]
'''
# 测试:
print(repr(trim('hello  ')))
print(repr(trim('  hello')))
print(repr(trim('  hello  ')))
print(repr(trim('  hello  world  ')))
print(repr(trim('')))
print(repr(trim('    ')))

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
'''

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):

    if not L:
        return (None, None)

    min_val = L[0]
    max_val = L[0]

    for i in L:
        if i > max_val:
            max_val = i
        
        if i < min_val:
            min_val = i
    
    return (min_val, max_val)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
