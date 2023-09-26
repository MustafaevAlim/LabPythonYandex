a = int(input())
b = int(input())
b, a = max(a, b), min(a,b)

while True:
    if b % a == 0:
        print(a)
        break
    else:
        b, a = a, b % a
    