strings = int(input())
columns = int(input())

numbers = len(str(columns * strings))
n = 0
for i in range(1, strings + 1):
    x = i
    while n < columns:
        print(f'{x :>{numbers}}', end=' ')
        x += strings
        n += 1
    print('')
    n = 0