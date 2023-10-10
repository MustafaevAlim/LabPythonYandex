s = ''.join(input().split())
if s.lower() == s.lower()[::-1]:
    print('YES')
else:
    print('NO')