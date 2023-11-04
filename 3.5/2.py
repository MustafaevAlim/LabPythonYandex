from sys import stdin

difference = []
for i in stdin:
    s = i.rstrip('\n').split()
    difference.append(int(s[2]) - int(s[1]))
print(round(sum(difference) / len(difference)))