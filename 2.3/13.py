n = int(input())

s = 'ЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯ'
for i in range(n):
    s1 = input()
    if s1 < s:
        s = s1

print(s)