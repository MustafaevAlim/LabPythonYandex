from itertools import product, accumulate

def povtor_10(x):
    if x.count(10) > 1:
        return False
    return True

def rabbit(start, finish, step):
    res = []

    for jumps in product([-3, -1, 1, 3], repeat=step):

        if sum(jumps) == finish - start:
            ans = ([start] + [start + i for i in accumulate(jumps)])
            if povtor_10(ans):
                res.append(ans)
    return res


result = rabbit(7, 10, 3)
print(*result, sep="\n")