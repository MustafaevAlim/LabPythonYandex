from itertools import product

n = int(input())
letters = set()
string = []
for i in range(n):
    s = input().split('-')
    string.append(set(s))
    [letters.add(j) for j in s]

ans = []
for i in product(*string):
    ans.append(''.join(i))

ans = sorted(ans)
for i in ans:
    print(i)
