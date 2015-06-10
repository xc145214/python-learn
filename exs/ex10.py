#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 函数的参数

# 一个参数


def power1(x):
    return x * x

print power1(5)

# 多个参数


def power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print power2(5)

print power2(4, 4)

# 学生注册 enroll()多参数


def enroll(name, gender, age=6, city='Beijing'):
    print 'name', name
    print 'gender', gender
    print 'age', age
    print 'city', city

enroll('Saral', 'F')

enroll('Bob', 'M', 7)

enroll('Adam', 'M', city='Tianjin')

# 定义函数的默认参数必须是不变的对象比如 string None


def add_end_1(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print add_end_1()

print add_end_1()

print add_end_1()

# 如果参数为可变对象


def add_end_2(L=[]):
    L.append('END')
    return L

print add_end_2([1, 2, 3])

print add_end_2(['x', 'y', 'z'])

print add_end_2()

print add_end_2()

# 计算 一组数的平方

# 使用列表参数


def calc_1(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 调用函数时 用list 或者 tuple
print calc_1([1, 2, 3])

print calc_1((1, 3, 6, 7))

# 使用可变参数


def cale_2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print cale_2(1, 2)

print cale_2()

print cale_2(1, 3, 5, 6)

# 如果已经有list 或者 tuple
nums = [1, 2, 3, 4]

print cale_2(*nums)		# 好的写法

nums = [1, 2, 3, 4]

print cale_2(nums[0], nums[1], nums[2], nums[3])

# 关键字参数


def person(name, age, **kw):
    print 'name', name, 'age ', age, 'kw', kw

person('Michael', 30)

person('Bob', 35, city='Beijing')

person('Adam', 45, gender='F', job='Engineer')

# 先组装成一个dict
kw = {'city': 'Beijing', 'job': 'Engineer'}

person('Jack', 23, city=kw['city'], job=kw['job'])

person('Jack', 23, **kw)  # 推荐写法


# 参数组合
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

func(1, 2)
func(1, 2, c=3)
func(1, 3, 4, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)

# 通过tuple  和 dict 调用
args = (1, 2, 3, 4)
kw = {'x': 99, 'y': 88}
func(*args, **kw)
