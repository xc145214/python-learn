#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 匿名函数

# lambda
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

f = lambda x: x * x

print f(5)


# 返回lambda
def build(x, y):
    return lambda: x * x + y * y

f1 = build(12, 13)
print f1
print f1()
