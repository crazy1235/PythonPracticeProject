# -*- coding: utf-8 -*-

# 列表
print '------------- 生成列表 ----------------'

print range(1, 10)

l = []
for x in range(1, 11):
    l.append(x * x)

print l

print '------------- 列表生成式 ----------------'

print [x * x for x in range(1, 11)]

# 使用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
print [x * (x + 1) for x in range(1, 101, 2)]

print '------------- 复杂表达式 ----------------'

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}
tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.iteritems()]
print '<table>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

# 字符串可以通过%进行格式化，用指定的参数代替%s。

print '------------- 条件过滤 ----------------'

# 列表生成式的for循环后面可以加上if判断
print [x * x for x in range(1, 20) if x % 3 == 0]


# 练习题目
# 写一个函数，接受一个list，然后把list中的所有字符串变大写后返回，非字符串元素将被忽略

def upperList(L):
    return [x.upper() for x in L if isinstance(x, str)]


print upperList(['Hello', 'world', 101])

print '------------- 多层表达式 ----------------'

print [m + n for m in 'ABC' for n in '123']

result = [a * 100 + b * 10 + c for a in range(1, 10) for b in range(0, 10) for c in range(0, 10) if a == c]
print len(result), result

result = [a for a in range(100, 1000) if a % 10 == a / 100]
print len(result), result
