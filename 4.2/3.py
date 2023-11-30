def count_del(x):
    s = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return s
    

def gcd(*numbers):
    s = set(i for i in range(1, 1000000))
    for i in numbers:
        s = s & count_del(i)
    s = sorted(s)
    return s[-1]

    
