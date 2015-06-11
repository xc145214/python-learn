#!/usr/bin/env python
# -*- coding: utf-8 -*-


# tuple 不可变列表

classmates =  ('Michael', 'Bob', 'Tracy')

# 访问：

print classmates[0]

print classmates[-1]

# 定义 空tuple

t = ()

# 定义只有1个元素的tuple

t = (1,)

# t不可变 它的元素可以变 可以是list

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t
