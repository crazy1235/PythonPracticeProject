# -*- coding: utf-8 -*-

# Python的集合类型
print '------------- Python的集合类型 ----------------'

print ['A', 'B', 'C']

names = ['jacksen', 'michael', 'Tom']
print names

emptyList = []
print emptyList

# 按照索引访问list
print names[1]
print names[0]
print names[len(names) - 1]

# 逆向取值 -- 不能越界！
# 天啦撸，竟然可以支持负数下标！！！！
print names[-0]
print names[-1]
print names[-2]
print names[-3]

# print names[-4]

# 添加新元素 - append
names.append("lincoln")
print names

# 插入新元素 - insert
names.insert(0, "sara")
print names
print names[-1]
names.insert(-1, "T-BAG")
print names

# 删除元素 - pop - 删掉list的最后一个元素，并会返回这个元素
print names.pop()
print names

print names.pop(-1)
print names

# 替换元素的值
names[-1] = "bruce"
print names

# tuple - 元组，一旦创建完毕，就不能修改！
# 准确的来说，tuple的元素指向不能变
print '------------- tuple ----------------'

tup = ('Adam', 'Lisa', 'Bart')
print tup

print tup[0]
print tup[2]
print tup[-1]

# Python规定，单元素tuple要多加一个逗号
tup = ()
print tup
tup = (23333) # 编译器会提示多余的括号！
print tup
tup = (2,)
print tup
