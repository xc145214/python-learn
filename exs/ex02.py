#!/usr/bin/env python
# -*- coding: utf-8 -*-

# list 操作

classmates = ['Michael', 'Bob', 'Tracy']

# 访问第一个元素

print classmates[0]

# 访问最后一个元素

print classmates[-1]

print classmates[len(classmates)-1]

# 添加一个元素

classmates.append('Adam')

print classmates

# 插入一个元素

classmates.insert(1,'Jack')

print classmates

# 删除末尾元素

classmates.pop()

# 删除指定位置元素

classmates.pop(1)


# 指定位置替换元素

classmates[1] = 'niao'

print classmates

# 嵌套元素

p =  ['asp', 'php']
s =  ['python', 'java', p, 'scheme']

print s