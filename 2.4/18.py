n = int(input())
x = 1
count = 0
strings = []
for i in range(1, n + 1):
    s = ''
    for j in range(i, i + x):
        if count >= n:
            break
        count += 1
        s += str(count) + ' '
    if s == '':
        break
    x += 1
    s = s[:-1]
    strings.append(s)

width = len(strings[-1])
for i in strings:
    print(f'{i :^{width}}')

