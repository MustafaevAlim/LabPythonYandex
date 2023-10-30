n = int(input())

products = []
for i in range(n):
    s = input().split(', ')
    products += s

products = sorted(products)
for n, s in enumerate(products, 1):
    print(f'{n}. {s}')