n = int(input())

first = (n % 10) + ((n % 100) // 10)
second = ((n%100) // 10) + (n // 100)

if first > second:
    print(str(first) + str(second))
else:
    print(str(second) + str(first))