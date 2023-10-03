n = int(input())
max_n = -10000000
s = ''
for i in range(n):
    name = input()
    number = input()
    summa = sum([int(x) for x in number])
    if summa >= max_n:
        max_n = summa
        s = name

print(s)