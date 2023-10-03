n = int(input())
s = ''
for i in range(n):
    b = input()
    maxim = max([int(x) for x in b])
    s += str(maxim)
print(s)