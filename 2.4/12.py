strings = int(input())
columns = int(input())

numbers = len(str(columns * strings))
n = 0
for i in range(strings):
    for j in range(1, columns + 1):
        n += 1
        print(f'{n :>{numbers}}', end=' ')
        if n % columns == 0:
            break
    print('')