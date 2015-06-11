#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 根据输入的时间判断年龄

birth = int(raw_input('birth: '))

if birth > 2000:
	print u'00后'
elif birth >1990:
	print u'90后'
elif birth >1980:
	print u'80后'
else:
	print u'automan'