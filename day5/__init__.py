# -*- coding: utf-8 -*-
import math

# 函数
print '------------- 函数 ----------------'

print 'python内置了很多函数'

print abs(100)
print abs(-12.34)

print cmp(1, 2)  # x < y, 返回 -1
print cmp(10.2, -23)  # x > y, 返回 1
print cmp(0, 0)  # x = y, 返回 0

print 'int()函数将其他数据类型转成整数'
print int(12.23)
print int('112')
# print int('abc')  #ValueError

print 'str()函数将其他数据类型转成str'
print str(123)
print str(1.00)
print str(0.000)
print str(-0)


# 定义函数

def square_of_sum(l):
    result = 0
    for x in l:
        result = result + x * x
    return result


print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-1, -2, -3, -4, -5])

# 函数返回多个值
print 'python可以返回多个值，这点很牛逼。相比java、c#这些语言只能返回单个值'


def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y + step * math.cos(angle)
    return nx, ny


# 直接打印结果法系那是一个tuple
print move(100, 200, 20, math.pi / 6)
nx, ny = move(100, 200, 20, math.pi / 6)
print nx, ny

print '------------------------'
print '求一个一元二次方程的解: ax² + bx + c = 0'


def quadratic_equation(a, b, c):
    t = math.sqrt(b * b - 4 * a * c)
    return (-b + t) / (2 * a), (-b - t) / (2 * a)


print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)

# 递归函数
print '------------- 递归函数 ----------------'


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print fact(10)
print fact(5)

print '使用递归函数要注意防止栈溢出'
print '计算机中，函数调用就是通过栈-stack来实现的。每当进入一个函数，栈就加一层；当函数返回，栈就减少一层。' \
      '由于栈的大小不是无限的，所以递归调用的次数过多，会导致栈溢出！'

# 默认参数
print '------------- 默认参数，只能定义在必须参数的后面 ----------------'

print int('12')
print int('12', 16)  # 第二个参数表示进制
print int('12', 8)


def power(x, n=2):
    result = 1
    while n > 0:
        n = n - 1
        result = result * x
    return result


print power(5)
print power(5, 1)
print power(5, 3)

# 可变参数
print '------------- 可变参数 ----------------'
print 'Python解释器会把传入的一组参数组装成一个tuple'


def average(*args):
    result = 0
    if len(args) == 0:
        return result
    for arg in args:
        result = result + arg
    return result / len(args)


print average()
print average(1, 2, 3, 4)
print average(12, 34)
