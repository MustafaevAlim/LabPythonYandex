from itertools import product, accumulate

def rabbit(start, finish, step):
    res = []

    for jumps in product([1, 2], repeat=step):

        if sum(jumps) == finish - start:
            res.append([start] + [start + i for i in accumulate(jumps)])
    return res


result = rabbit(1, 11, 6)
print(*result, sep="\n")