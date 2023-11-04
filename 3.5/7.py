num = []
with open(input(), 'r', encoding='utf-8') as f:
    for i in f.readlines():
        num.extend(list(map(int, i.rstrip().split())))
print(len(num))
print(len([x for x in num if x > 0]))
print(min(num))
print(max(num))
print(sum(num))
print(round(sum(num) / len(num), 2))