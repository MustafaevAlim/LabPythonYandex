def change_base(n, base):
    res = ''
    while n > 0:
        res += str(n % base)
        n //= base
    return res[::-1]


n = int(input())
max_summa = 0
max_ans = 0
for i in range(2, 11):
    summa = 0
    for j in change_base(n, i):
        summa += int(j)
    if summa > max_summa:
        max_summa = summa
        max_ans = i
print(max_ans)