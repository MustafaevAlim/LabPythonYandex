from itertools import product
card = ['пик', 'треф', 'бубен', 'червей']

s_card = input()
card.remove(s_card)

nominal = [str(i) for i in range(2,11)]
nominal += ['валет', 'дама', 'король', 'туз']
for i in product(nominal, card):
    print(*i)