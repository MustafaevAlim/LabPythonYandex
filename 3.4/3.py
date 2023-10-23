from itertools import count

start, finish, step = map(float, input().split())

for value in count(start, step):
    if value <= finish:
        print(round(value, 2))
    else:
        break