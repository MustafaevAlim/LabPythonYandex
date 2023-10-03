n = int(input())
count = 0
for i in range(n):
    b = input()
    if b == b[::-1]:
        count += 1
print(count)