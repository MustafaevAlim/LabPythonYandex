n = int(input())

n1 = n // 100
n2 =(n % 100) // 10
n3 = n % 10

max = -1000000
min = 1000000000
sr = 0
if n1 > n2 and n1 > n3:
    max = n1
    if n2 > n3:
        min = n3
    else:
        min = n2
    sr = (n1 + n2 + n3) - max + min
elif n2 > n1 and n2 > n3:
    max = n2
    if n1 > n3:
        min = n3
    else:
        min = n1
    sr = (n1 + n2 + n3) - max + min
elif n3 > n1 and n3 > n2:
    max = n3
    if n1 > n2:
        min = n2
    else:
        min = n1
    sr = (n1 + n2 + n3) - (max + min)

if max + min == sr * 2:
    print('YES')
else:
    print('NO')