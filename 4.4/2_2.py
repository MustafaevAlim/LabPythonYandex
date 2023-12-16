def add_word(word):
    x.append(word)

def get_work():
    s = ''
    for i in x:
        s += i + ', '
    s = s[:-2] + '.' + ' ' + f'({str(len(x))})'
    return s

x = []
add_word("мама")
add_word("мыла")
print(get_work())
add_word("раму")
print(get_work())