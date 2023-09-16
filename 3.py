n = int(input())
result = 0

for i in range(n):
    was_rabbit = False
    while ((object := input()) != 'ВСЁ'):
        if object == 'зайка':
            was_rabbit = True
    else:
        result += was_rabbit

print(result)