# Hanoi Tower
print 'a ------------> c'


def hanoi(n, a, b, c):
    if n == 1:
        move(n, a, c)
    else:
        hanoi(n - 1, a, c, b)
        move(n, a, c)
        hanoi(n - 1, b, a, c)


def move(n, x, y):
    print x, '-->', y, '~', n


print hanoi(3, 'a', 'b', 'c')
