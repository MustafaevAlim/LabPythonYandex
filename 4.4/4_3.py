def rindex(text):
    s = sorted(set(text))
    for i in s:
        if i != ' ':
            yield (i, text.index(i))

texter = 'Мама мыла раму'
for letter, count in rindex(texter):
    print(f"{letter}: {count}")