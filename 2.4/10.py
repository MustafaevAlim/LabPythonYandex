n = int(input())
print('А Б В')
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for z in range(1, n + 1):
            if i + z + j == n:
                print(i, j, z)