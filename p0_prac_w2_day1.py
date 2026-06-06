
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Bad Operand Type')
    if x >= 0:
        return x
    else:
        return -x


import math
def quadratic(a, b, c):
    if a ==0:
        raise TypeError('a must not be 0.') # early return / guard clause
    dlt = b ** 2 - 4 * a * c
    if dlt > 0:
        x1 = (-b + math.sqrt(dlt)) / (2 * a) 
        x2 = (-b - math.sqrt(dlt)) / (2 * a) 
        return x1,x2

    elif dlt == 0:
        x1 = -b / (2 * a) 
        x2 = x1
        return x1,x2
        
    else:
        return ("This system of two linear equations has no solution.") 
    

# 2235 Add Two Integers

def add_integer(num1, num2):
    return num1 + num2

print(add_integer(-10, 4))
print(add_integer(12,5))

#2413 Smallest Even Multiple

#Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.   


def SEM(n):
    if n % 2 == 0:
        return n
    else:
        return n*2

print(SEM(4))
print(SEM(5))   

'''
1768 Merge Strings Alternately:

You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''

def merge_string(word1, word2):

    length_w1 = len(word1)
    length_w2 = len(word2)
    min_len = min(length_w1, length_w2)
    merged_len = length_w1 + length_w2
    merged_str=[]
    for idx in range(0, merged_len):
        merged_str.append(' ')

    for i in range(0, min_len * 2, 2):
            merged_str[i] = word1[int(i/2)]

    for j in range(1, min_len * 2, 2):
            merged_str[j] = word2[int((j-1)/2)]
    
    if length_w1 - min_len == 0:
        pass
    else:
        for i in range(min_len * 2, merged_len):
                merged_str[i] = word1[i-min_len] 
    
    if length_w2 - min_len == 0:
        pass
    else:
        for i in range(min_len * 2, merged_len):
                merged_str[i] = word2[i-min_len]        
    
    final_str = "".join(merged_str)

    return final_str

print(merge_string("abcd", "ef"))
print(merge_string("ab", "pqrs"))