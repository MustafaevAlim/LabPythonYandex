s = ''
alf = 'йфячыцувсмакепитрнгоьблшщдюжзхэъabcdefghijklmnopqrstuvwxyz'
d = {a: x for a in alf for x in [0]}
ans_s = ''
while True:
    s = input().lower()
    if s.upper() == 'ФИНИШ':
        break
    ans_s += s

max_ans = -100000000
ans = ''
for i in alf:
    d[i] += ans_s.count(i)

for i in d:
    if d[i] > max_ans:
        max_ans = d[i]
        ans = i

print(ans)

