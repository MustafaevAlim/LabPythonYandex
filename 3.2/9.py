all_object = dict()
s = ' '
while s != []:
    s = input().split()
    for i in s:
        if i in all_object:
            all_object[i] += 1
        else:
            all_object[i] = 1

for i in all_object:
    print(i, all_object[i])