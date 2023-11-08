with open('secret.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        s = ''
        for j in i:
            if j == ' ':
                s += ' '
            else:
                s += chr(ord(j) & 255)
        print(s.strip())