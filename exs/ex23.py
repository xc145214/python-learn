#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 字符串转数字
print int('123456')

# 进制
print int('123456', base=8)

print int('123456',16)


# 2进制转换
def int2(x,base=2):
    return int(x,base)

print int2('1000000')
print int2('1010101')


# 偏函数

import functools
int2 = functools.partial(int,base=2)
print int2('1000000')
print int2('1010101')

# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

max2 = functools.partial(max,10)
print max2(5,6,7)