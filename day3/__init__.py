# -*- coding: utf-8 -*-

# if 语句
print '------------- if 语句 ----------------'

age = 23
if age >= 12:
    print 'I am not 12, I am only 23!'
    print 'haha~~'
print "end"

# if else
print '------------- if else ----------------'
if not age < 20:
    print 'come on baby!'

if age >= 30:
    print 'I am an old man!'
else:
    print 'I am a teenager!'

# if else if else
print '------------- if else if else ----------------'
if age >= 18:
    print 'adult'
else:
    if age >= 6:
        print 'teenager'
    else:
        if age >= 3:
            print 'kid'
        else:
            print 'baby'

print '------------ elif --> else if -------------'
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
elif age >= 3:
    print 'kid'
else:
    print 'baby'

# for 循环
print '------------- for 循环 ----------------'
names = ['micheal', 'lincoln', 'benjamin', 'john', 'fernando', 'sucre', 'bagel']
for name in names:
    print name

# while 循环
print '------------- while 循环 ----------------'
a = 10
b = 9
while a >= b:
    print b
    b = b + 1
print 'a = ', a, ' b = ', b

# break 退出循环
print '------------- break 退出循环 ----------------'

c = 20
while b < c:
    print b
    b = b + 1
    if b > 15:
        break
    print 'while ---'
print 'end b = ', b

# continue 继续循环
print '------------- continue 继续循环 ----------------'

d = 30
while b < d:
    b = b + 1
    if b < 25:
        continue
    print b
print 'end b = ', b

# 嵌套for循环
print '------------- 嵌套for循环 ----------------'

for x in ['A', 'B', 'C']:
    for y in ['1', '2', '3']:
        print x + y