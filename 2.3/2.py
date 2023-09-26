s = ''
z = 0
while s != 'Приехали!':
    s = input()
    if 'зайка' in s:
        z += 1
print(z)