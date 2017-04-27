# -*- coding: utf-8 -*-

# dict 数据字典
print '------------- dict 数据字典 ----------------'
nameAndScore = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print nameAndScore  # 注意输出的顺序！
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

# 更新dict
print '------------- dict 更新数据 ----------------'

nameAndScore['Lisa'] = 101
nameAndScore['Jacksen'] = 150
print nameAndScore

for key in nameAndScore:
    print key, ':', nameAndScore[key]

# set
print '------------- set ----------------'

# set持有一些列元素，但是不能重复，是无序的

# 创建set的方式是调用set()并传入list，list的元素将作为set的元素

s = set(['A', 'B', 'C', 'B'])
print s  # 注意观察打印顺序！

# 由于set是无序的，所以不能通过索引来访问！
print 'A' in s
print 'a' in s

weekdays = {'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'}
if 'WED' in weekdays:
    print 'OK'
else:
    print 'ERROR'

nameScoreSet = {('Adam', 95), ('Lisa', 85), ('Bart', 59)}

for nameScore in nameScoreSet:
    # print nameScore
    print nameScore[0], ':', nameScore[1]

# 更新set
print '------------- 更新 set ----------------'

print '如果已经存在了该元素，则不会加进去也不报错'

weekdays.add('SUN')
print weekdays

nameScoreSet.add(('Jacksen', 100))
print nameScoreSet
nameScoreSet.add(('Jacksen', 110))
print nameScoreSet
nameScoreSet.add(('Jacksen', 110))
print nameScoreSet

# 删除set元素
print '------------- 删除set元素 ----------------'

weekdays.remove('WED')
print weekdays

print '删除的元素不存在时，会报错！KeyError'
# weekdays.remove('ABC')
# print weekdays

key = 'ABC'
if key in weekdays:
    weekdays.remove(key)
else:
    print 'The Set does not has the', key, 'value.'

