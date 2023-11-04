with open(input(), 'r', encoding='utf-8') as f:
    n = int(input())
    [print(x.strip()) for x in f.readlines()[len(f.readlines()) - n:]]