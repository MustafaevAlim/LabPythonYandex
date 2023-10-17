def delet(n):
    s = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return s


numbers = map(int, input().split('; '))
numbers = set(numbers)
numbers = list(numbers)
numbers = sorted(numbers)
for i in range(len(numbers)):
    s = str(numbers[i]) + ' - '
    for j in range(len(numbers)):
        if len(delet(numbers[i]) & delet(numbers[j])) == 1:
            s += str(numbers[j]) + ', '
    if len(s) <= 5:
        continue
    print(s[:-2])