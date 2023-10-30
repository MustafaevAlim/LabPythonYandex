from itertools import product

n = int(input())
print('А Б В')
numbers = [i for i in range(1, n + 1)]
for n1, n2, n3 in product(numbers, numbers, numbers):
    if n1 + n2 + n3 == n:
        print(n1, n2, n3)