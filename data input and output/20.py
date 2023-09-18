n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())

y = abs((n * m - k1 * n) / (k1 - k2))
x = n - y
print(int(x), int(y))




