p = int(input())
v = int(input())
t = int(input())

if p > v > t:
    print('1. Петя')
    print('2. Вася')
    print('3. Толя')
elif v > p > t:
    print('1. Вася')
    print('2. Петя')
    print('3. Толя')
elif p > t > v:
    print('1. Петя')
    print('2. Толя')
    print('3. Вася')
elif v > t > p:
    print('1. Вася')
    print('2. Толя')
    print('3. Петя')
elif t > p > v:
    print('1. Толя')
    print('2. Петя')
    print('3. Вася')
elif t > v > p:
    print('1. Толя')
    print('2. Вася')
    print('3. Петя')