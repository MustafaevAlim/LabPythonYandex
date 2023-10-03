strings = int(input())
columns = int(input())

width = len(str(strings * columns))

chet_str = 0
nechet_str = 0
for i in range(1, strings + 1):
    n = 0
    if i % 2 != 0:
        while n < columns:
            nechet_str += 1
            print(f'{nechet_str :>{width}}', end=' ')
            n += 1
    else:
        chet_str = nechet_str + columns
        nechet_str = chet_str
        while n < columns:
            print(f'{chet_str :>{width}}', end=' ')
            chet_str -= 1
            n += 1
    print('')