s = ' '
while s != '':
    s = input()
    if s.endswith('@@@'):
        continue
    else:
        print(s.lstrip('##'))