n = int(input())

for i in range(n):
    s = input()
    end_s = int(s[:s.index('%')])
    s = s[s.index('%') + 1:]
    max_len = int(s[s.index('%') + 1:])
    s = s[:s.index('%')].strip()
    s = s[end_s::-3]
    s = s[:max_len]
    s = s[::-1]
    print(s)
