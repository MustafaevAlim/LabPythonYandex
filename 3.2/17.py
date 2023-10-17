acquaintances = {}
while True:
    s = input()
    if s == '':
        break
    name1, name2 = s.split()
    if name1 in acquaintances:
        acquaintances[name1].add(name2)
    else:
        acquaintances[name1] = {name2}
    if name2 in acquaintances:
        acquaintances[name2].add(name1)
    else:
        acquaintances[name2] = {name1}

ans_dict = {}
for i in acquaintances:
    acquaintances_lvl2 = set()
    for j in acquaintances[i]:
        if j == i:
            continue
        else:
            for x in acquaintances[j]:
                acquaintances_lvl2.add(x)
    acquaintances_lvl2.remove(i)
    acquaintances_lvl2 = acquaintances_lvl2 - acquaintances[i]
    acquaintances_lvl2 = sorted(acquaintances_lvl2)
    ans_dict[i] = acquaintances_lvl2

ans_dict = dict(sorted(ans_dict.items()))

for key, value in ans_dict.items():
    s = ''
    for i in value:
        s += i + ', '
    s = s[:-2]
    print(f'{key}: {s}')