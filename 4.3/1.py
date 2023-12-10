def recursive_sum(*n):
    n = list(n)
    if len(n) == 0:
        return 0
    a = n.pop()
    return a + recursive_sum(*n)
