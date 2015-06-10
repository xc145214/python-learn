#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 迭代

# for in
l = [1,2,3,4]
t = (1,2,3,4)
s = set([1,2,3,4])

for x in l:
	print x

for x in t:
	print x

for x in s:
	print x

# dict 遍历
d = {'a':1,'b':2,'c':3}
for key in d:
	print key

for value in d.itervalues():
	print value


for k,v in d.iteritems():
	print k,v


# 字符串 遍历
for ch in 'ABCD':
	print ch

# 判断对象是否可迭代
from collections import Iterable

print isinstance('abc',Iterable)
print isinstance([1,2,3],Iterable)
print isinstance(123,Iterable)

# list取下标
for index,value in enumerate(['A','B','C']):
	print index,value

# for 循环 2个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print x,y
