from sys import stdin

for i in stdin:
    s = i.rstrip('\n')
    if s.startswith('#'):
        continue
    elif '#' in s:
        print(s[:s.index('#')].rstrip())
    else:
        print(s)