# -*- coding: utf-8 -*-

print ('hello   python!!!')

# 注释
print '------------- Unicode字符串 ----------------'

# #号后面的表示注释的内容
print 'Hope is a good thing, maybe the best of things and no good thing ever dies!'  # 肖申克的救赎里面经典台词!

# Unicode 字符串
print '------------- Unicode字符串 ----------------'

print u'你好，python'

print u'''静夜思\n
床前明月光，
疑是地上霜，
举头望明月，
低头思故乡。'''

print ur'''我的中文名字叫闫森, My english name is "jacksen"'''

# 整数与浮点数
print '------------- 整数与浮点数 ----------------'
# 支持对整数和浮点数直接进行四则运算
print 1 + 2 - 3
print 3 * 5 / 10
print 3 * 5 % 10
print 1.2 * 2.3 + 3.4 / 0.34 - 0.5
# 括号提升优先级，并且括号可以嵌套多层
print (1 + 3) * 4
print (10.2 - 2.3) * (5 / 2 - 3.6) + 1
# 整数运算结果仍是整数，浮点数运算结果是浮点数
# 整数与浮点数运算结果是浮点数

# 布尔类型
print '------------- 布尔类型 ----------------'

# 布尔类型只有True和False两种值，注意大小写
# 与运算 主要有一个为False结果就为False，两个布尔值都是True时结果才是True
print True and True
print True and False
print False and False
print False and True

print True & True
print True & False
print False & False
print False & True

# 或运算 只要有一个为True，结果就是True
print True or True
print True or False
print False or True
print False or False

print True | True
print True | False
print False | True
print False | False

print '\n'

# 非运算 把True变为False，把False变为True
print not True
print not False

print ~True
print ~False
