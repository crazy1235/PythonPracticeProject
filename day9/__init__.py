# -*- coding: utf-8 -*-
import math

# 高阶函数
print '------------- 高阶函数 ----------------'


# 能接受函数做参数的函数叫做高阶函数

def add(x, y, f):
    return f(x) + f(y)


print add(1, -3, abs)

print add(25, 9, math.sqrt)

# math.sqrt() 的结果是浮点数

# map()函数
print '------------- map()函数 ----------------'


def sqrtList(x):
    return x * x


print map(sqrtList, [1, 2, 3, 4, 5, 6])


def formatStr(s):
    return s[0].upper() + s[1:].lower()


print map(formatStr, ['adam', 'JACKSEN', 'bar1'])

# reduce()函数
print '------------- reduce()函数 ----------------'


def prod(x, y):
    return x * y


print reduce(prod, [1, 2, 3, 4, 5])

print reduce(prod, [1, 2, 3, 4, 5], 2)

# filter()函数
print '------------- filter()函数 ----------------'

print 'filter()函数接受一个函数f和一个list，这个函数f的作用是对每个元素进行判断' \
      '返回True或者False，filter()根据判断结果自动过滤掉不符合条件的元素，' \
      '返回由符合条件元素组成的新list'


def is_not_empty(s):
    return s and len(s.strip()) > 0


print filter(is_not_empty, ['test', None, '', 'str', ' ', 'END', False])

print '利用filter过滤掉1~100中平方根是整数的数'


def is_sqr(n):
    return n * n in range(1, 101)


print map(sqrtList, filter(is_sqr, range(1, 101)))

# 自定义排序函数
print '------------- 自定义排序函数 ----------------'

# sorted()
print sorted([2, -1, 23, -0, 24])

print 'sorted() 可以接收一个比较函数来实现自定义排序， 类似于java里面的 Collections.sort'


def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0


print sorted([2, -1, 23, -0, 24], reversed_cmp)

print 'sorted()也可以对字符串进行排序，字符串默认是按照ASCII大小来比较的'
print sorted(['abc', 'bac', '123', 'Zab', 'jack', '##', '**', ' ', ''])


def cmp_ignore_case(a, b):
    a = a.upper()
    b = b.upper()
    if a > b:
        return 1
    if a < b:
        return -1
    return 0


print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

# 返回函数
print '------------- 返回函数 ----------------'


# 注意区分返回值和返回函数
# 对返回的函数进行调用时，才得到结果


def calc_prod(lst):
    def list_prod():
        return reduce(prod, lst)

    return list_prod


re = calc_prod([1, 2, 3, 4, 5])
print re()

# 闭包
print '------------- 闭包 ----------------'
print '内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包(closure)'


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print f1(), f2(), f3()


def _count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j

            return g

        r = f(i)  # 值
        fs.append(r)
    return fs


f1, f2, f3 = _count()
print f1(), f2(), f3()

# 匿名函数
print '------------- 匿名函数 ----------------'
print '匿名函数只能有一个表达式，不写return'
print map(lambda x: x * x, [1, 2, 3, 4, 5])

print sorted([1, 3, 0, -3, 5], lambda x, y: -cmp(x, y))


