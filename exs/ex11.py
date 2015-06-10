#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 递归函数

# 阶乘函数


def fact_1(n):
    if n == 1:
        return 1
    return n * fact_1(n - 1)


def fact_2(n):
    if n == 1:
        return 1
    for i in range(1, n + 1):
        sun = 1
        for j in range(1, i + 1):
            sun = sun * j
    return sun

print fact_1(1)
print fact_2(1)

print fact_1(5)
print fact_2(5)

print fact_1(100)
print fact_1(100)

# 递归数据溢出
#print fact_1(1000)
print fact_2(1000)