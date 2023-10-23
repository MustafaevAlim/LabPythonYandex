first_group = [i for i in input().split(', ')]
second_group = [i for i in input().split(', ')]
for h1, h2 in zip(first_group, second_group):
    print(f'{h1} - {h2}')