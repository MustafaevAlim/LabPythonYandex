s1 = input().split(', ')
s1 += input().split(', ')
s1 += input().split(', ')

s1 = sorted(s1)
numbers = [i for i in range(1, len(s1) + 1)]
for n, s in zip(numbers, s1):
    print(f'{n}. {s}')