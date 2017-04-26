# -*- coding: utf-8 -*-

# dict 数据字典
print '------------- dict 数据字典 ----------------'
nameAndScore = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print nameAndScore # 注意输出的顺序！

print 'the length of nameAndScore is', len(nameAndScore)

print 'the score of "Adam" is ', nameAndScore['Adam']

# 只要key存在，dict就返回对应的value。如果key不存在，直接报错：KeyError
# 可以先判断一下key是否存在
name = 'Lisa1'
if name in nameAndScore:
    print 'the score of ', name, ' is ', nameAndScore[name]
else:
    print 'there is no one called', name
# 或者通过dict的get方法，当key不存在时，返回None
print nameAndScore.get('Bart', 100)
# 也可以为get函数设置默认值
print nameAndScore.get('Bart1', 100)

# dict的查找速度快， 时间复杂度是o(1)
# list的查找速度随着元素的增加而逐渐下降，时间复杂度是o(n)
# dict就类似于java中的数组，list类似于java中的list

# 由于dict是按key查找的，所以一个dict中，key不能重复！
# dict的key-value是无序的！

# dict的key必须不可变！

