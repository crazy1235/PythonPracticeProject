# -*- coding: utf-8 -*-

# 迭代
print '------------- 迭代 ----------------'

print '---- enumerate()函数 -----'
L = ['Adam', 'Lisa', 'Bart', 'Paul']

for index, name in enumerate(L):
    print index, '-', name

print '实际上enumerate()函数将迭代的每个元素变成了tuple'
print "[(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]"

for l in enumerate(L):
    index = l[0]
    name = l[1]
    print index, ':', name

for index, name in enumerate(L):
    print index, ':', name

# range()函数
print 'range(1, ?)函数可以创建出起始为1的数列'
for index, name in zip(range(1, len(L) + 1), L):
    print index, '#', name

# 迭代dict的value

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}
for i in d:
    print i, d[i]

# values()
print d.values()
for v in d.values():
    print v

# print d

# itervalues()
print d.itervalues()

print 'values()方法实际上把一个dict转成了包含value的list'
print 'itervalues()方法不会转换，会在迭代过程中依次从dict中取出value, 所以itervalues()方法比values()节省了内存'

print ''

# 迭代dict的key和value
print d.items()

print 'items() 方法把dict对象转换成了包含tuple的list'

for key, value in d.items():
    print key, ':', value

print d.iteritems()

for key, value in d.iteritems():
    print key, ':', value

#
print "d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }" \
      "打印出 name : score，最后再打印出平均分 average : score。"

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}
result = 0
for key, value in d.iteritems():
    result = result + value
    print key, ':', value
print 'average', ':', result / len(d)
