import json


n1, n2 = [input() for _ in range(2)]

with open(n1, mode='r', encoding='utf-8') as f:
    data1 = json.load(f)

with open(n2, mode='r', encoding='utf-8') as f:
    data2 = json.load(f)

data3 = {}

for i in range(len(data1)):
    name = list(data1[i].items())[0][1]
    for k, v in data1[i].items():
        if k == "name":
            data3[name] = {}
        else:
            data3[name][k] = v

for i in range(len(data2)):
    name = list(data2[i].items())[0][1]
    for k, v in data2[i].items():
        if k == "name":
            continue
        elif k in data3[name]:
            if data3[name][k] < v:
                data3[name][k] = v
        else:
            data3[name][k] = v


with open(n1, mode='w', encoding='utf-8') as f:
    json.dump(data3, f, ensure_ascii=False, indent=4)