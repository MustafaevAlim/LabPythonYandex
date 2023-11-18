import json
from sys import stdin


numbers = []
digits = set()
for i in stdin:
    for j in i:
        digits.add(j)
    numbers.append(int(i.rstrip()))

ans = {}
for i in digits:
    for j in numbers:
        if i in str(j):
            if i not in ans:
                ans[i] = [j]
            else:
                ans[i].append(j)

for i in ans:
    ans[i] = sorted(set(ans[i]))
with open('result.json', 'w', encoding='utf-8') as file_out:
    json.dump(ans, file_out, indent=4)