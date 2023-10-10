cereals = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']

n = int(input())
count = 0
for i in range(n):
    if count >= len(cereals):
        count = 0
    print(cereals[count])
    count += 1
