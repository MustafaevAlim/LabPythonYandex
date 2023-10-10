def change2(arr, a):
    arr.pop()
    arr.pop()
    arr.append(a)
    return arr


def change1(arr, a):
    arr.pop()
    arr.append(a)
    return arr


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


string = input().split()
n = []
actions = []
for i in string:
    if i in '+-*/~!#@':
        if i == '+':
            new_n = n[-1] + n[-2]
            n = change2(n, new_n)
        elif i == '*':
            new_n = n[-1] * n[-2]
            n = change2(n, new_n)
        elif i == '-':
            new_n = n[-2] - n[-1]
            n = change2(n, new_n)
        elif i == '/':
            new_n = n[-2] // n[-1]
            n = change2(n, new_n)
        elif i == '~':
            new_n = -1 * n[-1]
            n = change1(n, new_n)
        elif i == '!':
            new_n = factorial(n[-1])
            n = change1(n, new_n)
        elif i == '#':
            new_n = n[-1]
            n.append(new_n)
        elif i == '@':
            new_n = [n[-2], n[-1], n[-3]]
            n.pop()
            n.pop()
            n.pop()
            n += new_n
    else:
        n.append(int(i))
print(*n)