d = {}

s = ' '
while True:
    s = input()
    if s == '':
        break
    s = s.split()
    for i in s:
        length = len(i)
        if length not in d:
            d[length] = [i.upper()]
        else:
            d[length].append(i.upper())

for i in d:
    s = str(i) + ': '
    for j in sorted(list(set(d[i])), reverse=True):
        s += j + '; '
    print(s[:-2])