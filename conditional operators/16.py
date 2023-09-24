p = int(input())
v = int(input())
t = int(input())

if p > v and p > t:
    first = 'Петя'
    if v > t:
        second = 'Вася'
        third = 'Толя'
    else:
        second = 'Толя'
        third = 'Вася'
elif v > p and v > t:
    first = 'Вася'
    if p > t:
        second = 'Петя'
        third = 'Толя'
    else:
        second = 'Толя'
        third = 'Петя'
elif t > p and t > v:
    first = 'Толя'
    if p > v:
        second = 'Петя'
        third = 'Вася'
    else:
        second = 'Вася'
        third = 'Петя'
print(f'{first :^24}')
print(f'  {second :<22}')
print(f'{third :>22}  ')
print(f'{"II" :^8}{"I" :^8}{"III" :^8}')