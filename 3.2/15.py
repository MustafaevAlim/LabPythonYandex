numbers = map(int, input().split())
numbers = [bin(x)[2:] for x in numbers]

dict_list = []
for i in numbers:
    dict_n = {}
    dict_n['digits'] = len(i)
    dict_n['units'] = i.count('1')
    dict_n['zeros'] = i.count('0')
    dict_list.append(dict_n)

print(dict_list)