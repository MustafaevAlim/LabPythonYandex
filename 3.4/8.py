from itertools import cycle

n = int(input())
porridge = []
for i in range(n):
    s = input()
    porridge.append(s)

menu = int(input())
count = 1
for i in cycle(porridge):
    if count > menu:
        break
    print(i)
    count += 1
