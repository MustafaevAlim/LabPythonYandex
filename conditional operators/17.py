a = float(input())
b = float(input())
c = float(input())

if a == b == c == 0:
    print('Infinite solutions')

D = (b ** 2) - 4 * a * c
if a != 0:
    if D < 0:
        print('No solution')

    if D > 0:
        x1 = (((-b) + (D ** 0.5)) / (2 * a))
        x2 = (((-b) - (D ** 0.5)) / (2 * a))
        if x1 > x2:
            print(f"{x2 :.2f} {x1 :.2f}")
        else:
            print(f"{x1 :.2f} {x2 :.2f}")

    if D == 0:
        x = (-b) / (2 * a)
        print(f"{x :.2f}")
if a == 0:
    if b != 0:
        x = (-c) / b
        print(f'{x :.2f}')
    else:
        print('No solution')
    