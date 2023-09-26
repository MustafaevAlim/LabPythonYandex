n = int(input())

n = str(n)
flag = True
for i in range(len(n)):
    if n[i] != n[-1-i]:
        flag = False


if flag:
    print('YES')
else:
    print('NO')