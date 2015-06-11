#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 函数

# 引入math包
import math

# 计算面积


def area_of_circle(r):
    if not isinstance(r, (int, float)):
        raise TypeError('bad operand type')
    return math.pi * r * r

r = 12.34
print area_of_circle(r)

# 求和函数


def sum_num(n):
    sum = 0
    # 求和
    for x in n:
        sum += x
    return sum


print sum_num(range(1, 101))

# 函数嵌套调用


def fun1(n):
    l = []
    for x in range(1, n + 1):
        l.append(x * x + 1)
    return l

print sum_num(fun1(100))


# 定义函数　my_abs()
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print my_abs(-1.23)

# my_abs('AA')
# 定义空函数


def nop():
    pass

age = 12
if age >= 18:
    pass


# 返回多个值

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x, y

r = move(100, 100, 60, math.pi / 6)

print r

# 实际上返回的是个tuple
