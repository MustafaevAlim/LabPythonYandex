n = int(input())
x = 1
count = 0
for i in range(1, n + 1):
    for j in range(i , i + x):
        if count >= n:
            break
        count += 1
        print(count, end=' ')
    print('')
    x += 1
