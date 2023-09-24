a = int(input())
b = int(input())
c = int(input())

if a ** 2 < b ** 2 + c ** 2 and b ** 2 < a ** 2 + c ** 2 and c ** 2 < a ** 2 + b ** 2:
    print('крайне мала')
elif max(a, b, c) ** 2 > min(a, b, c) ** 2 + ((a + b + c) - (min(a, b, c) + max(a, b, c))) ** 2:
    print('велика')
elif max(a, b, c) ** 2 == min(a, b, c) ** 2 + ((a + b + c) - (min(a, b, c) + max(a, b, c))) ** 2:
    print('100%')