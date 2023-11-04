import json
with open(input(), 'r', encoding='utf-8') as f:
    number = []
    for i in f.readlines():
        number.extend(list(map(int, i.rstrip().split())))
    ans = {}
    ans['count'] = len(number)
    ans['positive_count'] = len([x for x in number if x > 0])
    ans['min'] = min(number) 
    ans['max'] = max(number)
    ans['sum'] = sum(number)
    ans['average'] = round(sum(number) / len(number), 2)
with open(input(), 'w', encoding='utf-8') as f_json:
    json.dump(ans, f_json, ensure_ascii=False, indent=2)


