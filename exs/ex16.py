#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 列表生成器 generator

L = [x * x for x in range(10)]
print L

g = (x * x for x in range(10))
print g


# g 保存的是算法 调用next 方法
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()

# for循环遍历
for n in g:
    print n


# 斐波拉契数列
def fib_1(m):
    n, a, b = 0, 0, 1
    while n < m:
        print b
        a, b = b, a + b
        n = n + 1
fib_1(6)

# 生成generator



def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

print fib(6)


for x in fib(100):
	print x


#变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

def odd():
	print 'step 1'
	yield 1
	print 'step 2'
	yield 3
	print 'step 3'
	yield 5

o = odd()

o.next()
o.next()
o.next()
# o.next()