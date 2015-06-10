#!/usr/bin/env python
# -*- coding: utf-8 -*-

# filter　过滤

# 求奇数


def is_odd(n):
    return n % 2 == 1
print filter(is_odd, range(1, 17))

# 过滤空字符串


def not_empty(s):
    return s and s.strip()

print filter(not_empty, ['A', '', 'B', None, 'C', '  '])


# 过滤素数
def is_prime(n):
    for x in range(2, n - 1):
        if n % x == 0:
            return x

print filter(is_prime, range(1, 101))
