import json
from sys import stdin

name_data = input()
ans = {}
for i in stdin:
    s = i.split(' == ')
    ans[s[0].rstrip()] = s[1].rstrip()

with open(name_data, 'r', encoding='utf-8') as file_in:
    old = json.load(file_in)

with open(name_data, 'w', encoding='utf-8') as file_out:
    new = old | ans
    json.dump(new, file_out, ensure_ascii=False, indent=2)

