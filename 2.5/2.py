s = input()
n1 = int(input())
n2 = int(input())
if 'sum' in s:
    print(n1 + n2)
elif 'sub' in s:
    print(n1 - n2)
elif 'mult' in s:
    print(n1 * n2)
elif 'div' in s:
    print(n1 // n2)