n = int(input())
width = int(input())
for i in range(1, n + 1):
    s = ''
    for j in range(1, n + 1):
        s += f'{i * j :^{width}}' + '|'
    print(s[:-1])
    if i != n:
        print('-' * len(s[:-1]))