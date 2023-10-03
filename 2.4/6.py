def count_del(x):
    s = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return s


s = {i for i in range(1, 10000)}
n = int(input())
for i in range(n):
    b = int(input())
    s = s.intersection(count_del(b))


print(max(sorted(s)))




