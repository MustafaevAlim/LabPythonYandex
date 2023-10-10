len_s = int(input())
n = int(input())
for i in range(n):
    s = input()
    if len(s) > len_s:
        print(s[:len_s - 3] + '...')
    else:
        print(s)
