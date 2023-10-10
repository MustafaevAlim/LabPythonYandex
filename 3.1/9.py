s = ' '
while s != '':
    s = input()
    if s == '':
        break
    if s[0] == '#':
        continue
    print(s[:s.index('#')].strip())