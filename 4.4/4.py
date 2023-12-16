def counter(text):
    s = sorted(set(text.replace(' ', '')))
    for i in s:
        yield (i, text.count(i))

texter = 'Мама мыла раму'
for letter, count in counter(texter):
    print(f"{letter}: {count}")