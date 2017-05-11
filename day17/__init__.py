# -*- coding: utf-8 -*-
import re

# 正则表达式
print '-------------- 正则表达式 ---------------'

# re模块

pa = re.compile(r'abc')
ma = pa.match('abc 123 abc')
print ma.group()
print ma.span()
print len(ma.group())

#
pa = re.compile(r'abc', re.I)
ma = pa.match('aBc 21abc')
print ma.group()

#
pa = re.compile(r'(abc)', re.I)
ma = pa.match('aBc 21 abc')
print ma.groups()

#
ma = re.match(r'ab', 'abc b')
print ma.group()

# []

pa = re.compile('[a-zA-Z0-9]')
ma = pa.match('0abc123')
print ma.group()
