from itertools import product

n, m = int(input()), int(input())
len_column = len(str(n * m))
for i in range(n):
    line = product(range(1, m + 1), [i * m])
    print(*[f'{j : >{len_column}}' for j in list(map(lambda x: sum(x), line))])