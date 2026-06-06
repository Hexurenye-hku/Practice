'''
杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

# 规律:
# 首尾永远是 1
# 中间 index i = 上一行 [i-1] + [i]
# generator 要自己记住当前行，每次 yield 之后算出下一行

def triangles():
    current = [1]
    while True:
        yield current
        current = [current[i-1] + current[i]  for i in range(1, len(current))]
        current = [1] + current + [1]
    

#test

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

'''



# 1.clean_input(s)：去掉首尾空格，中间多余空格压缩成一个
def clean_input(s):
    s = s.strip()
    text = s.split()
    s = ' '.join(text)
    return s

# print(clean_input("          Happy Labors   day  to Everybody!    "))

# 2.count_vowels(s)：返回元音字母 aeiou 的个数
def count_vowels(s):
    s = s.lower()
    total = 0

    for i in ['a', 'e', 'i', 'o', 'u']:
        num_i = s.count(i)
        total += num_i 
    
    return total

# print(count_vowels("hi, I'm Bruce. How are you and where are you from?"))

# 3.replace_sensitive(s)：把字符串里所有"密码"替换成"***"
def replace_sensitive(s):

    s = s.replace('密码', '***')
    return s

# print(replace_sensitive('My 密码 is rosebud123.'))

# 4.find_first_number(s)：找第一个数字字符的位置，没有返回 -1
def find_first_number(s):

    for i,v in enumerate(s):
        if v.isdigit():
            return i
    
    return -1    

# print(find_first_number('My 密码 is rosebud123 123.'))
    
# 5.join_words(words)：输入单词列表，用 " | " 拼接成字符串
def join_words(words):
    return ' | '.join(words)
    

print(join_words(['hello', 'world', 'python']))


