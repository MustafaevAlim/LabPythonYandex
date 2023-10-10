n = int(input())
for i in range(n):
    s = input()
    if s.count('зайка') == 0:
        print('Заек нет =(')
    else:
        print(s.index('зайка') + 1)