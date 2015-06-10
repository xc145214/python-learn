#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 列表生成式

# 生成列表1-10
L = range(1, 11)

print L

# 生成列表 1x1 ,2x2 ……

L = []
for x in range(1, 11):
    L.append(x * x)

print L

# 简便方式

L = [x * x for x in range(1, 11)]
print L

L = [x * x for x in range(1, 11) if x % 2 == 0]
print L

# 字符组合
L = [m + n for m in 'ABC' for n in 'XYZ']
print L

# 列出文件目录
import os  # 导入os模块，模块的概念后面讲到
dirs = [d for d in os.listdir('.')]  # os.listdir可以列出文件和目录
print dirs

# 多变量 for in

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.iteritems():
    print k, '= ', v


# dict to list
d = {'x': 'A', 'y': 'B', 'z': 'C'}
L = [k + ' = ' + v for k, v in d.iteritems()]
print L

# 字符转换大小写
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]


# 过滤其他
L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() for s in L if isinstance(s,str)]