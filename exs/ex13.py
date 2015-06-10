#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 获取 list 或 tuple 的部分元素列表

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 笨方法

L1 = [L[0], L[1], L[2]]
print L1

# 循环
r = []
n = 3
for i in range(n):
    r.append(L[i])

print r

# 切片 倒数 -1  正数 1

print L[:3]

print L[1:3]

print L[-1]

print L[-1:-2]

print L[-2]

print L[-2:-1]

# 切片取值
L = range(100)
print L

# 前10
print L[:10]

# 后10
print L[-10:]

# 11-20
print L[10:20]

# 前 10个数中的偶数
print L[:10:2]

# 隔5 取数
print L[::5]

# 复制新数组
print L[:]


# tuple
t = (0,1,2,3,5,4)
print t[:3]

# 字符串
s1 = 'ABCDEFG'[:3]
s2 = 'ABCDEFG'[::2]

print s1
print s2