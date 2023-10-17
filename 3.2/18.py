n = int(input())
tresuare = {}
for i in range(n):
    x, y = map(int, input().split())
    x //= 10
    y //= 10
    if (x, y) not in tresuare:
        tresuare[(x, y)] = 1
    else:
        tresuare[(x, y)] += 1
print(max(tresuare.values()))