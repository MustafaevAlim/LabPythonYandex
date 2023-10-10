len_s = int(input())
n = int(input())
s = []
for i in range(n):
    s.append(input())

count_char = 0
for i in s:
    if count_char > len(s):
        print(i[:len_s - count_char - 3] + '...')
        break
    print(i)
    count_char += len(i)
