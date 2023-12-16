from itertools import product, accumulate

def povtor(lst):
    for i in lst:
        if lst.count(i) > 1:
            return False
    return True

def rabbit(start, finish, step):
    res = []

    for jumps in product([-1, 1, 2], repeat=step):

        if sum(jumps) == finish - start:
            ans = [start] + [start + i for i in accumulate(jumps)]
            if povtor(ans):
                res.append(ans)
    return res


result = rabbit(13, 17, 4)
print(*result, sep="\n")