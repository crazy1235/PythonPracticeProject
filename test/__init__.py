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
confusion[01] = 5
confusion[01.00] = 6
confusion[1 + 2] = 7
confusion[-0.0] = 8
confusion[0] = 9
print confusion

print '---------------------------'


def print_header(str):
    print '+++%s+++' % str


print_header.category = 1
print_header.text = 'some info'
print_header('%d %s' % (print_header.category, print_header.text))
