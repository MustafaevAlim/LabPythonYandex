strings = int(input())
columns = int(input())
count = 1
width = len(str(strings * columns))
array = [[0 for i in range(strings)] for j in range(columns)]
for i in range(columns):
    for j in range(strings):
        array[i][j] = count
        count += 1
    if i % 2 != 0:
        array[i].reverse()
for i in range(strings):
    for j in range(columns):
        print(' ' * (width- len(str(array[j][i]))), array[j][i], end=' ', sep='')
    print()