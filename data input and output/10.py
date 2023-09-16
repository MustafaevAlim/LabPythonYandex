name = input()
wardrobe = int(input())

group = wardrobe//100
number_bed = (wardrobe//10) % 10
number_in_list = wardrobe % 10

print(f'Группа №{group}')
print(f'{number_in_list}. {name}')
print(f'Шкафчик: {wardrobe}')
print(f'Кроватка: {number_bed}')