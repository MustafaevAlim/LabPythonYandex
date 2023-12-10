def make_equation(*n):
    n = list(n)
    if len(n) == 1:
        return n[0]
    a = n.pop()
    return f'({make_equation(*n)}' + f') * x + {a}'


