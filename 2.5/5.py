n = int(input())
maxim = -1000000000
for i in range(n):
    a = []
    while True:
        s = input()
        if s == 'next':
            break
        a.append(int(s))
    sr = round(sum(a) / len(a), 2)
    if sr > maxim:
        maxim = sr

print(maxim)