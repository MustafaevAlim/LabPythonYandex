from sys import stdin

palidromic = set()
for i in stdin:
    s = i.rstrip('\n').split() 
    for j in s:
        if j.lower() == j[::-1].lower():
            palidromic.add(j)


palidromic = sorted(palidromic)
for i in palidromic:
    print(i)