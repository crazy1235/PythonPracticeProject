# -*- coding: utf-8 -*-
import types

# 类 & 实例

print '--------- 类 & 实例 --------'

print '类通过class关键字定义。类名以大写字母开头'


class Person(object):
    print 'person', __name__


jack = Person()
print jack
jack.name = "jack"
jack.age = 25

sen = Person()
print sen
sen.name = "sen"
sen.age = 26
sen.school = "henan university"

per_list = sorted([jack, sen], lambda a, b: cmp(a.name, b.name))
print per_list

print per_list[0].name, per_list[1].name

# 初始化实例属性
print '---------- 初始化实例属性 -----------'
print '__init__()方法的第一个参数必须是self，后序参数可以自由指定；\n' \
      '创建实例时，必须提供self以外的参数'


class Person(object):
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


xiaoming = Person("xiaoming", 20, 175)

print xiaoming.name, xiaoming.age, xiaoming.height


# 任意关键字参数


class Person(object):
    def __init__(self, name, **kw):
        self.name = name
        for k, v in kw.iteritems():
            setattr(self, k, v)


pony = Person("马化腾", age=45)
print pony.name, pony.age

# 访问限制
print '-------------- 属性访问限制 ---------------'
print 'python对属性权限的控制是通过属性名来实现的，如果一个属性由双下划綫开头(__)，该属性无法被外部访问'


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__job = 'CEO'


Michael = Person("Micheal", 50)
print Michael.name, Michael.age
# print Michael.__job

print '如果一个属性以"__xxx__"的形式定义，则又可以被外部访问了，这种形式的属性在Python中称为特殊属性，' \
      '有很多预定义的特殊属性可以使用，通常不要把不同属性用这种形式定义'

# 类属性

print '------------ 类属性 -------------'


class Person(object):
    address = "Earth"

    def __init__(self, name):
        self.name = name


p1 = Person('p1')
print p1.address
p2 = Person('p2')
print p2.address
Person.address = "hangzhou"
print p1.address, p2.address
p2.address = "China"
print p1.address, p2.address
Person.address = "beijing"
print p1.address, p2.address

# 实例属性和类属性重名时，实例属性优先级高

del p2.address
print p1.address, p2.address

# 定义实例方法
print '----------------- 定义实例方法 ----------------'
print '实例方法的定义第一个参数永远也是self'


class Person(object):
    def __init__(self, name):
        self.__name = name  # 不让直接访问, 通过get方法

    def get_name(self):
        return self.__name


jingjing = Person('jingjing')
print jingjing.get_name()

print '---------------------------'

print '方法也是属性，所以，可以动态的将方法添加到实例上，只需要用types.MethodType()把一个函数变成一个方法'


def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'


class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


p1 = Person('Bob', 79)
p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
print p1.get_grade()

print '给一个实例动态添加方法并不常见，直接在class类中定义更加直观'

print '----------------------'
print '和属性类似，方法也分实例方法和类方法'

print '通过标记一个@classmethod，将一个方法绑定到类上，这样就是一个类方法'
print '由于是在类上调用，而非实例上调用，因此类方法无法获得任何实例变量，只能获取类的引用'


class Person(object):
    __count = 0

    @classmethod
    def how_many(cls):
        return cls.__count

    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1


print Person.how_many()
p1 = Person("nike")
print Person.how_many()
p2 = Person("leo")
print Person.how_many()
