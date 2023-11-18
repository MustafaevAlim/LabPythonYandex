from itertools import product

n = int(input())
letters = set()
for i in range(n):
    s = input().split('-')
    [letters.add(j) for j in s]

print(letters)
letters = sorted(letters)
for i in product(letters, repeat=n):
    print(i)
