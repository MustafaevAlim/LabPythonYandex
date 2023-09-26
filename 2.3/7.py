a = int(input())
b = int(input())

minim = 1000000
for i in range(a * b, 1, -1):
    if i % a == 0 and i % b == 0:
        minim = min(i, minim)

print(minim)