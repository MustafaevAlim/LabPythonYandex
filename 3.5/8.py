lst1 = []
lst2 = []
with open(input(), 'r', encoding='utf-8') as f:
    for i in f.readlines():
        lst1.extend(i.strip().split())
with open(input(), 'r', encoding='utf-8') as f:
    for i in f.readlines():
        lst2.extend(i.strip().split())

lst1 = set(lst1)
lst2 = set(lst2)
with open(input(), 'w', encoding='utf-8') as f:
    ans = (lst1 | lst2) - (lst1 & lst2)
    ans = sorted(ans)
    for i in ans:
        f.write(i + '\n')