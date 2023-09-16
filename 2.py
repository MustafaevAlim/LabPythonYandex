coor = [0,0]

while (direction := input()) != 'СТОП':
    if direction == 'СЕВЕР':
        coor[0] += int(input())
    elif direction == 'ЮГ':
        coor[0] -= int(input())
    elif direction == 'ВОСТОК':
        coor[1] += int(input())
    else:
        coor[1] -= int(input())


else:
    print(coor)