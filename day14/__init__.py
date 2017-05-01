# -*- coding: utf-8 -*-

# 类的继承
print '------------ 类的继承 ------------'


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score


class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

    def print_info(self):
        print 'name:', self.name, ', gender:', self.gender, ', course:', self.course


t = Teacher("Tom", 'Female', 'English')
print t.print_info()

# 判断类型
print '------------- isinstance()判断变量类型 ---------------'

p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 90)

print isinstance(p, Person)
print isinstance(s, Person)
print isinstance(t, Person)

print isinstance(s, Student)
print isinstance(s, Teacher)
print isinstance(t, Teacher)
print isinstance(t, Student)

print isinstance(p, object)
print isinstance(s, object)
print isinstance(t, object)

# 多态
print '----------- 多态 -----------'

# 多重继承
print '----------- 多重继承 -----------'


class A(object):
    def __init__(self, a):
        print 'init A...'
        self.a = a


class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print 'init B...'


class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print 'init C...'


class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print 'init D...'


d = D('d')

print '虽然A被继承了两次，但是__init__()只调用了一次'
print '多重继承的目的是从两种继承树中分别选择并继承出子类，以便组合功能使用'

# 获取对象信息
print '---------------- 获取对象信息 --------------'

print 'type()函数获取变量的类型，返回一个Type对象'
print type(123)
print type('abc')
print type([1, 3, 5])
print type({"a": 1, "b": 2})
print type(d)
print type(s)
print type(object)
print type(p)

print 'dir()函数获取变量的所有属性'
print dir(123)
print dir('abc')
print dir([1, 2, 3])
print dir({'a': 1, 'b': 2})
print dir(d)
print dir(s)
print dir(object)
print dir(p)
