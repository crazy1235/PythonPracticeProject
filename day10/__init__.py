# -*- coding: utf-8 -*-

print '------------- 子类重写数据 ----------------'


class Parent(object):
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print Parent.x, Child1.x, Child2.x
Child1.x = 2
print Parent.x, Child1.x, Child2.x
Parent.x = 3
print Parent.x, Child1.x, Child2.x

# Python中，类变量在内部作为字典处理的。
# 如果一个变量的名字没有在当前类的字典中发现，将搜索祖先类知道被引用的变量名被找到
# 如果这个被引用的变量名既没有在自己所在的类又没有在祖先类中找到，会引发一个AttributeError异常
# 被重写的值在父类中改变只会影响到未重写该值的子类中的值
