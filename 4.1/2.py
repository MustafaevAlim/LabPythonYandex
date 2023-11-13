def delet(x):
    s = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return s


def gcd(first, second):
    return sorted((delet(first) & delet(second)))[-1]
