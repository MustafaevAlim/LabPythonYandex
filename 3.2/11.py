
n = int(input())
name_list = []
for i in range(n):
    name = input()
    name_list.append(name)

count = 0
for i in name_list:
    if name_list.count(i) > 1:
        count += 1

print(count)
