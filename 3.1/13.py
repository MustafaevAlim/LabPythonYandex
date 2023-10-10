n = int(input())

number = []
for i in range(n):
    number.append(int(input()))

degree = int(input())
for i in map(lambda x: x ** degree, number):
    print(i)