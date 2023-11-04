from sys import stdin

summma = 0
for i in stdin:
    summma += sum(list(map(int, i.rstrip('\n').split())))
print(summma)