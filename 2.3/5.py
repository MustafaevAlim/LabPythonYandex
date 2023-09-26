summa = 0
n = 1
while n != 0:
    n = int(input())
    if n >= 500:
        summa += n * 0.9
    else:
        summa += n
print(summa)
