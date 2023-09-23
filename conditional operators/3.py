p = int(input())
v = int(input())
t = int(input())

if p > v > t:
    print('Петя')
elif v > p > t:
    print('Вася')
else:
    print('Толя')