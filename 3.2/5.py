n = int(input())
m = int(input())
name = []
for i in range(n + m):
    name.append(input())

ans = []
for i in name:
    if name.count(i) == 1:
        ans.append(i)

if len(ans) == 0:
    print('Таких нет')
else:
    print(len(ans))
