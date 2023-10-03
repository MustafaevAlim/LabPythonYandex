n = int(input())

summa = 0
for i in range(n):
    b = input()
    summa += sum([int(x) for x in b])

print(summa)
