from itertools import permutations


n = int(input())
products = []
for i in range(n):
    s = input().split(', ')
    products += s
products = sorted(products)

for i in permutations(products, 3):
    print(' '.join(i))
