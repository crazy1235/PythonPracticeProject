# -*- coding: utf-8 -*-

# 切片-slice
print '------------- 切片 ----------------'

L = ['Adam', 'Lisa', 'Bart', 'Paul']
print L
r = []
for i in range(3):
    r.append(L[i])

print r

print '----- Python提供了切片(Slice)操作符 ----'
print 'L[a:b]表示取出从索引a到索引b的元素，但是不包括索引b'
print L[0:3]
print L[0:5]

print 'L[:]实际上表示赋值出来一个新的list'
print L[:]

print 'L[::2]表示每个2个元素取出一个'
print L[0:3:2]

# 倒序切片
print '------------- 倒序切片 ----------------'
print L[0:-1]
print L[-3:]
print L[-4:-1:2]

# practice
L = range(1, 101)
print len(L), L
print '前10个数:', L[0:10]
print '3的倍数:', L[2::3]
print '不大于50的5的倍数:', L[4:50:5]
print '最后10个数:', L[-10:]
print '最后10个5的倍数:', L[-46::5]
print '最后10个5的倍数:', L[4::5][-10:]  # 先找出所有5的倍数，然后去最后10个

# 字符串切片
print '------------- 字符串切片 ----------------'

s = 'abcdefg'
print s
print s[0:4]
print s[-3:]
print s[0:6:2]

# 其它高级语言对应的字符串截取操作都可以通过切片操作来完成

print '设计一个函数，接受一个字符串，然后返回一个仅首字母变成大写字母的字符串'


def firstCharUpper(s):
    return s[0].upper() + s[1:]

print firstCharUpper('abc')
print firstCharUpper('hello, python!')
print firstCharUpper('Jacksen')
