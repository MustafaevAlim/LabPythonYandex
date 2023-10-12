n = int(input())
name_and_porridge = list()

for i in range(n):
    name, *porridge = input().split()
    name_and_porridge.append((name, porridge))


porridge = input()
flag = False
ans = []
for i in name_and_porridge:
    if porridge in i[1]:
        ans.append(i[0])
        flag = True

ans = sorted(ans)
if flag == False:
    print('Таких нет')
else:
    for i in ans:
        print(i)





