seen = set()
while True:
    s = input()
    if s == '':
        break
    s = s.split()
    for i in range(len(s)):
        if s[i] == 'зайка':
            if i == 0:
                seen.add(s[i + 1])
            elif i == len(s) - 1:
                seen.add(s[i - 1])
            else:
                seen.add(s[i - 1])
                seen.add(s[i + 1])
for i in seen:
    print(i)