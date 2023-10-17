n = int(input())
kids = {}
for i in range(n):
    name, toys = input().split(': ')
    set_toys = set(toys.split(', '))
    kids[name] = set_toys
res = set()


for i in kids:
    toys = kids[i].copy()
    for j in kids:
        if i != j:
            toys.difference_update(kids[j])
    res.update(toys)
print(*sorted(list(res)), sep='\n')