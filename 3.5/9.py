with open(input(), 'r', encoding='utf-8') as f1:
    with open(input(), 'w', encoding='utf-8') as f2:
        for i in f1.readlines():
            if '\t' in i:
                i = i.replace('\t', '')
            s = list(map(lambda x: x.strip(), i.strip().split()))
            if len(s) != 0:
                if len(s) > 1:
                    print(' '.join(s), file=f2)
                else:
                    print(s[0], file=f2)
                    