n = int(input())
products = set()
for i in range(n):
    product = input()
    products.add(product)

m = int(input())
recipes = {}
for i in range(m):
    recipe = input()
    n = int(input())
    ingredients = set()
    for i in range(n):
        ingredient = input()
        ingredients.add(ingredient)
    recipes[recipe] = ingredients


ans = []
for i in recipes:
    if products >= recipes[i]:
        ans.append(i)

ans = sorted(ans)
if len(ans) == 0:
    print('Готовить нечего')
else:
    for i in ans:
        print(i)