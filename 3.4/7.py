from itertools import combinations

n = int(input())
name = []
for i in range(n):
    s = input()
    name.append(s)

for n1, n2 in combinations(name, 2):
    print(f'{n1} - {n2}')