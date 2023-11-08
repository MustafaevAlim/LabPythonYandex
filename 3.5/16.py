from sys import stdin

search = input().replace(' ','').lower()
files = []
for file in stdin:
    files.append(file.rstrip("\n"))

flag = False
for i in files:
    with open(i, 'r', encoding='utf-8') as f:
        s = ''
        for j in f.readlines():
            s += j.strip().replace(' ','').lower()
        if search in s:
            flag = True
            print(i)

if flag == False:
    print('404. Not found')