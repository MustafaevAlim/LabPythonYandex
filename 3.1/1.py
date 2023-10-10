n = int(input())

flag = True
for i in range(n):
    b = input()
    if b[0] not in 'абв':
        flag = False

if flag:
    print('YES')
else:
    print('NO')