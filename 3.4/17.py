from itertools import product, permutations

cards_ro = sorted(["бубен", "пик", "треф", "червей"])
card, rem_nom, situation = input(), input(), input()
best_card = [s for s in cards_ro if s.startswith(card[0:3])][0]
nominal = sorted(["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"])
nominal.remove(rem_nom)
comb = permutations(product(nominal, cards_ro), 3)
y = sorted(set([', '.join(' '.join(j) for j in sorted(i)) for i in comb]))
triads = [i for i in y if best_card in i]
for ind, triad in enumerate(triads):
    if triad == situation:
        print(triads[ind + 1])
        break