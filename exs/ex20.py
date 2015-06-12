#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 函数作为返回值

# 普通求和


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

print calc_sum(1, 2, 3, 3, 4, 5, 6)

# 返回函数


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum

f = lazy_sum(1, 3, 4, 5, 6)
print f

print f()


# f() 与 f1 互不影响
f1 = lazy_sum(1, 3, 4, 5, 6)
print f1 == f


# 闭包

# 返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs =[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print f1()
print f2()
print f3()

#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    fs =[]
    for i in range(1,4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs

f1,f2,f3 = count()
print f1()
print f2()
print f3()