n = int(input())
zayka = 0
falg = False
for i in range(n):
    s = ''
    while s != 'ВСЁ':
        s = input()
        if s == 'зайка':
            flag = True
    if flag:
        zayka += 1
print(zayka)