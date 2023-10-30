from itertools import permutations, product

cards = sorted(['бубен', 'пик', 'треф', 'червей'])
nominal = [str(i) for i in range(2, 11)]
nominal += ['валет', 'дама', 'король', 'туз']
print(nominal)
nominal = sorted(nominal)


s = input()
nominal_new = input()
if s == 'пики':
    s = 'пик'
elif s == 'трефы':
    s = 'треф'
elif s == 'буби':
    s = 'бубен'
elif s == 'черви':
    s = 'червей'
card = s
nominal.remove(nominal_new)

count = 0
for n1, n2, n3 in permutations(product(nominal, cards), 3):
    if count == 10:
        break
    if (card in n1) or (card in n2) or (card in n3):
        print(', '.join(list([' '.join(n1), ' '.join(n2), ' '.join(n3)])))
        count += 1
    else:
        continue