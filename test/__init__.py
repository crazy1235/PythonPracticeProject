# -*- coding: utf-8 -*-

names1 = ['Amir', 'Barry', 'Chales', 'Dao']
names2 = names1
names3 = names1[:]

print names1
print names2
print names3

print '---------------------------'

names2[0] = 'jack'

print names1
print names2
print names3

print '---------------------------'

confusion = {}
confusion[1] = 1
confusion[1.0] = 2
confusion[1.1] = 3
confusion['1'] = 4

print confusion

