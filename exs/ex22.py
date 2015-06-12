#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 装饰器


# 函数赋值
def now():
    """print the date"""
    print '2013-12-25'

f = now
print f()

# 获取函数的属性
print now.__name__
print f.__name__

# 输出注释
print f.__doc__

# 装配器
def log(func):
    def wrapper(*args,**kw):
        print 'call %s()' % func.__name__
        return func(*args,**kw)
    return wrapper


@log # now = log(now)
def now():
    print '2013-12-25'

now()

def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print '%s %s ():' % (text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute') # now = log('execute')(now)
def now():
    print '2013-12-25'

now()

print now.__name__

# functools.wraps 的使用
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator



