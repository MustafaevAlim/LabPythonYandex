m = int(input())
n = int(input())
step = (n - m) % 10

s = ''
for i in range(n, m + 1, step):
    s += str(i) + ', '
print(s[:-2])