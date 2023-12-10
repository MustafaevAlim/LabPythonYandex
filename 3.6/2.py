d = {}

s = ' '
while True:
    s = input()
    if s == '':
        break
    s = s.split()
    for i in s:
        if len(i) % 2 == 0:
            j = i[(len(i) // 2) - 1].lower()
        else:
            j = i[(len(i) // 2)].lower()
        if j not in d:
            d[j] = [i.upper()]
        else:
            d[j].append(i.upper())

for i in d:
    s = str(i) + ' "'
    for j in sorted(list(set(d[i]))):
        s += j + '. '
    print(f'{s[:-2]}"')