n = int(input())

name_dict = dict()
name_list = []
for i in range(n):
    name = input()
    name_list.append(name)

name_list = sorted(name_list)
for i in name_list:
    if i in name_dict:
        name_dict[i] += 1
    else:
        name_dict[i] = 1


if sum(name_dict.values()) == len(name_dict.keys()):
    print('Однофамильцев нет')
else:
    for i in name_dict:
        if name_dict[i] > 1:
            print(f'{i} - {name_dict[i]}')