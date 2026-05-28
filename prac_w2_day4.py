# Ex7.3
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错,
# 使用内建的isinstance函数可以判断一个变量是不是字符串
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
'''
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
'''

# Ex 1 max_in_list(nums)：输入一个数字列表，返回最大值。禁止用内置 max()。
from sympy import count_ops


def max_in_list(nums):
    if not nums:
        raise ValueError("列表不能为空") 
    
    max_val = nums[0]

    for i in nums:
        if i > max_val:
            max_val = i
    
    return max_val

# Ex 2 count_words(text)：输入一段英文字符串，返回每个单词出现次数的字典。
# 需求如下：
'''
输入：一个英文字符串，例如 "hello world hello python world hello"

输出: 一个字典, key 是单词, value 是该单词出现的次数，例如 {"hello": 3, "world": 2, "python": 1}

限制：不能用 Counter, 其他都可以用。

不需要处理：标点符号、大小写统一——输入的字符串是干净的，单词之间只有空格，全是小写。
'''

'''
我的思路是分2步走
第一步: 取出字符串text中的所有单词进入word_list, 然后去重;
第二步: 遍历word_list找出所有单词和它的个数, 写入word_dict.
'''
def count_words(text):
    if not text:
        raise ValueError('字符串不能为空')
    
    words_list = text.split()

    word_dict = {}

    word_clean = []


    for i in words_list: # 1.遍历 words_list 建 word_clean_去重
        
        if i not in word_clean:
            word_clean.append(i)


    word_dict = {key : '' for key in word_clean} # 2.用 word_clean 建 word_dict

    for key in word_dict: # 3.遍历 word_dict 数每个词的次数
        count = 0
        for i in words_list:
            if i == key:
                count += 1
        
        word_dict[key] = count

    return word_dict


# 你用了 word_clean 列表来去重，然后再建字典。
# 其实可以省掉这一步——遍历 words_list 时直接判断 if i not in word_dict，去重和计数可以一步完成。你现在的写法多绕了一圈。
# 问题是：第 1 步和第 3 步都在遍历 words_list，能不能只遍历一次,同时完成去重和计数？
def countw_opt(text):
    if not text:
        raise ValueError('字符串不能为空')
    
    words_list = text.split()

    word_dict = {}

    for i in words_list:
        if i not in word_dict:
            word_dict[i] = 1
        
        else:
            word_dict[i] += 1
    
    return word_dict


    
print(countw_opt("hello world hello python world hello"))
print(countw_opt("hello"))
print(countw_opt("a a a a a"))
print(countw_opt("one two three"))
print(countw_opt(""))    


        

        




