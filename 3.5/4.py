from sys import stdin

headings = []
for i in stdin:
    headings.append(i.rstrip('\n')) 

word = headings.pop(-1).lower()

for i in headings:
    if word in i.lower():
        print(i)