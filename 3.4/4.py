from itertools import accumulate

s = input().split()
s = ['*' + x for x in s]
for i in accumulate(s):
    print(i.replace('*', ' ').strip())
