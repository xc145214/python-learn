#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 模块


' a test module '

__author__ = 'xc'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print 'hello world'
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arugments!'

# 入口
if __name__ == '__main__':
    test()


# 别名
try:
    import json  # python >= 2.6
except ImportError:
    import simplejson as json  # python <= 2.5

# private


def _private_1(name):
    return 'Hello,%s' % name


def _private_2(name):
    return 'Hi,%s' % name

# public


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
