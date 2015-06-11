#!/usr/bin/env python
# -*- coding: utf-8 -*-

# set 集合 不重复

# 创建[1,2,3,4,1,2,4] 是一个参数 不是list
s = set([1, 2, 3, 4, 1, 2, 4])

print s

# 添加元素

s.add(6)

s.add('name')

print s

# 遍历

for item in s:
    print item

# 删除元素

if 6 in s:
    s.remove(6)

print s

# set 可以看做为数学的无序不重复集合 可以进行集合运算

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

print s1 & s2

print s1 | s2

# 可以通过tuple list创建 set
t = (1, 2, 3, 4, 5)
s = set(t)
print s

l = [1, 2, 3, 4, 5]
print set(l)

# 以下不行
t1 = (1, 2, 3, [4, 5])
l1 = [1, 2, 3, [4, 5]]
#s = set(l1)
#s = set(t1)
