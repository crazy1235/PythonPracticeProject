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
