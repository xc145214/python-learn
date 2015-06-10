#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 传入函数做参数


def add(x, y, f):
    return f(x) + f(y)


print add(-5, 6, abs)


# map 函数
def f(x):
    return x * x

print map(f, range(1, 11))

# 原始方式
L = []
for x in range(1, 11):
    L.append(f(x))

print L

# map 字符串
print map(str, range(1, 11))


# reduce 函数 reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 1--100 求和
def add_1(x, y):
    return x + y

print reduce(add_1, range(1, 101))


# 将字符转换为数字
def fn_1(x, y):
    return 10 * x + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print map(char2num, '12345')

print reduce(fn_1, map(char2num, '13452'))

# 数字字符串转数字


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]	#dictp[key]
    return reduce(fn, map(char2num, s))

print str2int('123452142')

# lambda 表达式


def str2int_1(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print str2int_1('12342124')


# map 处理字符大些


def format_word(l):
    def set_first_letter_big(s):
        return s.upper()[0] + s.lower()[1:]
    return map(set_first_letter_big, l)

l = ['adam', 'LISA', 'barT']
print format_word(l)

# 求和


def pop(list1):
    return reduce(lambda x, y: x * y, list1)

l = [1, 2, 3, 4, 5]
print pop(l)
