n = int(input())
head = []
for i in range(n):
    head.append(input())

search = input()

for i in head:
    if search in i.lower():
        print(i)