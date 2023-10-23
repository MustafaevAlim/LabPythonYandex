n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

maxim = -1000000000000
for i in range(1, n):
    if numbers[i] < numbers[i-1] and numbers[i] > maxim:
        maxim = numbers[i]
print(maxim)