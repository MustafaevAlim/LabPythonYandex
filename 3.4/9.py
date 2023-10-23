from itertools import product

n = int(input())
strings = [i for i in range(1, n + 1)]
columns = strings.copy()

numbers = []
for s, c in product(strings, columns):
    numbers.append(str(s * c))
    if len(numbers) == n:
        print(' '.join(numbers))
        numbers = []