#!/usr/bin/env python
# -*- coding: utf-8 -*-

# for  in 循环

names = ['Michael', 'Bob', 'Tracy']

for name in names:
	print name


# range() 函数
print range(5)


sum = 0 
for x in range(1,10):
	sum = sum + x
print sum

# 计算0-100之和

sum = 0 
for x in range(100):
	sum += x
print sum

# while 循环

sum = 0
n = 99
while n>0:
	sum += n
	n -= 2
print sum

