n = int(input())
meals = set()
for i in range(n):
    meal = input()
    meals.add(meal)

m = int(input())
cooked_dishes = set()
for i in range(m):
    count_meal = int(input())
    for j in range(count_meal):
        food = input()
        cooked_dishes.add(food)

ans = sorted(meals - cooked_dishes)

if len(ans) == 0:
    print('Готовить нечего')
else:
    for i in ans:
        print(i)