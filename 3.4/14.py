from itertools import permutations


n = int(input())
names = []
for i in range(n):
    names.append(input())

names = sorted(names)

for i in permutations(names, 3):
    print(', '.join(i))
