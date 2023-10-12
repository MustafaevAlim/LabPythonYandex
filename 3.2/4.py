n = int(input())
m = int(input())

love_semolima = set()
love_oatmeal = set()
for i in range(n):
    b = input()
    love_semolima.add(b)
for i in range(m):
    b = input()
    love_oatmeal.add(b)

ans = love_oatmeal.intersection(love_semolima)
if len(ans) == 0:
    print('Таких нет')
else:
    print(len(ans))