# -*- coding: utf-8 -*-

# 文件操作
print '------------- 文件操作 -------------'

type_1 = '├── '
type_2 = '│   ├── '
type_3 = '│   └── '
type_4 = '├── '
type_5 = '└── '

L = []
aFile = open('../a.txt')

line = aFile.readline().strip('\n')
while line != '':
    print line
    t = line.split(type_1)
    if len(t) >= 2:
        L.append(t[-1])
    elif len(line.split(type_2)) >= 2:
        L.append(line.split(type_2)[-1])
    elif len(line.split(type_3)) >= 2:
        L.append(line.split(type_3)[-1])
    elif len(line.split(type_4)) >= 2:
        L.append(line.split(type_4)[-1])
    elif len(line.split(type_5)) >= 2:
        L.append(line.split(type_5)[-1])
    line = aFile.readline().strip('\n')

print L

# print aFile.readlines()

# print '├──'
# print '─'
# a = '│   └── local.yaml'
# print a.split('├── ')




print '---------------- 练习题 ---------------------'


def proc1():
    j, k = 3, 4
    print 'j == %d and k == %d' % (j, k)
    k = 5


def proc2():
    j = 6
    proc1()
    print 'j == %d and k == %d' % (j, k)

k = 7
proc1()
# print 'j == %d and k == %d' % (j, k)

j = 8
proc2()
print 'j == %d and k == %d' % (j, k)
