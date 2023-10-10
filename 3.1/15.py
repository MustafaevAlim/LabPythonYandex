def delet(n):
    s = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n//i)
    return s

numbers = list(map(int, input().split()))

s = {i for i in range(1,1000000)}
for i in numbers:
    s = s.intersection(delet(i))

print(sorted(s)[-1])

