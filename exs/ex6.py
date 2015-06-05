#!/usr/bin/env python
# -*- coding: utf-8 -*-

# dict Map集合

# 创建map
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# 转换创建map
d = {}

names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

for i in range(len(names)):
    d[names[i]] = scores[i]

print d

# 添加元素 重复元素被替换

d['Adam'] = 67

d['Jack'] = 90

d['Jack'] = 88

print d

# 判断元素是否存在

if 'thomas' in d:
	print 'thomas in'
else:
	print 'thomas not in'

if d.get('Jack'):
	print 'Jack in'
else:
	print 'Jack not in'

print d.get('thomas',-1)
print d.get('thomas')
print d.get('Jack')

# 删除元素
if 'Bob' in d:
	d.pop('Bob')

print d

