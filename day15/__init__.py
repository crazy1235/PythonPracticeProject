# -*- coding: utf-8 -*-

# python的特殊方法
print '-------------- python的特殊方法 -------------'

print '__str__'
print '__len__'
print '__cmp__'

print '__getattr__'
print '__setattr__'
print '__delattr__'


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)


tom = Person('Tom', 'Male')
print tom

print 'python定义了__str__()和__repr__()两种方法'

# __cmp__
print '----------- __cmp__ -----------'

print '对int，str等内置数据类型排序时，python的sorted()按照默认的比较函数cmp排序，' \
      '但是，如果对一组Student类的实例排序时，就必须提供我们自己的特殊方法__cmp__()'


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, other):
        if self.score > other.score:
            return 1
        elif self.score < other.score:
            return -1
        else:
            return 0


L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 77)]
print sorted(L)

print '如果list不仅仅包含 Student 类，则 __cmp__ 可能会报错' \
      '所以可以定义一个函数过滤掉不是Student类的项'


def isStudent(x):
    if isinstance(x, Student):
        return True
    else:
        return False


L = [Student('Tim', 99), Student('Bob', 88), 100, 'Hello']
print sorted(filter(isStudent, L))

#  __len__

print '----------- __len__ -----------'


class Fib(object):
    def __init__(self, x):
        res = []
        a = 0
        b = 1
        while x > 0:
            res.append(a)
            t = a
            a = b
            b = t + b
            x = x - 1
        self.nums = res

    def __str__(self):
        return str(self.nums)

    __repr__ = __str__

    def __len__(self):
        return len(self.nums)


f = Fib(6)
print f
print len(f)

print 'a, b = b, a + b  等价于 \n' \
      't = a \n' \
      'a = b \n' \
      'b = t + b \n'

# 数学运算

print '---------- 数学运算 --------'


# 有理数运算
class Rational(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Rational(self.a * other.b + self.b * other.a, self.b * other.b)

    def __sub__(self, other):
        return Rational(self.a * other.b - self.b * other.a, self.b * other.b)

    def __mul__(self, other):
        return Rational(self.a * other.a, self.b * other.b)

    def __div__(self, other):
        return Rational(self.a * other.b, self.b * other.a)

    def __str__(self):
        return '%s/%s' % (self.a, self.b)

    __repr__ = __str__


r1 = Rational(1, 3)
r2 = Rational(1, 2)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2

# 类型转换
print '--------------- 类型转换 ---------------'

print int(12.34)
print float(1234)
print int(1 / 2)
print 1 / 2
print 1 // 2


class Rational(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __int__(self):
        return self.a // self.b

    def __float__(self):
        return float(self.a) / self.b


print float(Rational(7, 2))
print float(Rational(1, 3))

# @property
print '------------ @property ---------------'


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    @property
    def grade(self):
        if self.score < 60:
            return 'C'
        if self.score < 80:
            return 'B'
        return 'A'


s = Student('Jack', 60)
print s.grade
s.score = 80
print s.score
print s.grade
# s.score = 101
# print s.score


# __slots__

print '-------------- __slots__ -------------'

print 'python是动态语言，可以在运行期间动态添加属性' \
      '如果要限制添加的属性，就可以利用__slots__来实现！'
print '__slots__是指一个类允许的属性列表'


class A(object):
    def __init__(self, name):
        self.name = name


a = A('jack')
print a.name
a.name = 'jacksen'
print a.name
a.age = 25
print a.age


class B(object):
    __slots__ = ('name', 'age')

    def __init__(self, name):
        self.name = name


b = B('sen')
print b.name
b.name = 'jacksen'
print b.name
b.age = 20
print b.age
# b.gender = 'male'
# print b.gender

print '__slots__的目的是限制当前类所拥有的属性，如果不需要添加任意动态的属性，使用__slots__也能节省内存'

# __call__

print '------- __call__ --------'


class C(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print 'My name is %s ...' % self.name
        print "My friend's name is %s ..." % friend


c = C('jack', 'male')
print c('sen')
