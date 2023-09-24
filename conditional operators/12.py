side1 = int(input())
side2 = int(input())
side3 = int(input())

if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
    print('YES')
else:
    print('NO')