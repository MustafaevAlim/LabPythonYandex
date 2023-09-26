x = 0
y = 0
s = ''
while s != 'СТОП':
    s = input()
    if s != 'СТОП':
        n = int(input())
        if s == 'СЕВЕР':
            x += n
        elif s == 'ЮГ':
            x -= n
        elif s == 'ВОСТОК':
            y += n
        elif s == 'ЗАПАД':
            y -= n
print(x)
print(y)