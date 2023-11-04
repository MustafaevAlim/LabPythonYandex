import json

with open(name_file := input(), encoding='utf-8') as f:
    old_data = json.load(f)

with open(input(), encoding='utf-8') as f:
    new_data = json.load(f)


updates_data = []
for i in range(len(old_data)):
    updates_data.append({})
    for j in old_data[i]:
        if j not in updates_data[i]:
            updates_data[i][j] = old_data[i][j]
    for x in new_data[i]:
        if x not in updates_data[i]:
            updates_data[i][x] = new_data[i][x]
        elif new_data[i][x] > updates_data[i][x]:
            updates_data[i][x] = new_data[i][x]




users_data = {}
for data in updates_data:
    for j in data:
        if j == 'name':
            users_data[data[j]] = {}
            name = data[j]
        else:
            if j not in users_data[name]:
                users_data[name][j] = data[j]

with open(name_file, 'w', encoding='utf-8') as file_out:
    json.dump(users_data, file_out, ensure_ascii=False, indent=4)