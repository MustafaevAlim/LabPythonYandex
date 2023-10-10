string = input().split()
n = []
actions = []
for i in string:
    if i in '+-*':
        if i == '+':
            new_n = n[-1] + n[-2]
            n.pop()
            n.pop()
            n.append(new_n)
        elif i == '*':
            new_n = n[-1] * n[-2]
            n.pop()
            n.pop()
            n.append(new_n)
        elif i == '-':
            new_n = n[-2] - n[-1]
            n.pop()
            n.pop()
            n.append(new_n)
    else:
        n.append(int(i))
print(*n)