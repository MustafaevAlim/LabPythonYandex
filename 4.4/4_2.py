def rindex(text):
    s = sorted(set(text.replace(' ', '')))
    for i in s:
        yield (i, text.rfind(i))

texter = 'Мама мыла раму'
for letter, count in rindex(texter):
    print(f"{letter}: {count}")