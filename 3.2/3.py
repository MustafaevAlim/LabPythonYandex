n = int(input())
set_object = set()
for i in range(n):
    object = input().split()
    for j in object:
        set_object.add(j)

for i in set_object:
    print(i)