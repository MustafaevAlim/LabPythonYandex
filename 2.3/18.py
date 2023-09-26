n= int(input())
i = 2
s = ''
while i * i <= n:
    while n % i == 0:
        s += f' {i}'
        n = n / i
    i = i + 1
if n > 1:
    s += f' {int(n)}'
print(' * '.join(s.split()))