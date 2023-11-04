let = {
    "А": "A",
    "а": "a",
    "Б": "B",
    "б": "b",
    "В": "V",
    "в": "v",
    "Г": "G",
    "г": "g",
    "Д": "D",
    "д": "d",
    "Е": "E",
    "е": "e",
    "Ё": "E",
    "ё": "e",
    "Ж": "Zh",
    "ж": "zh",
    "З": "Z",
    "з": "z",
    "И": "I",
    "и": "i",
    "Й": "I",
    "й": "i",
    "К": "K",
    "к": "k",
    "Л": "L",
    "л": "l",
    "М": "M",
    "м": "m",
    "Н": "N",
    "н": "n",
    "О": "O",
    "о": "o",
    "П": "P",
    "п": "p",
    "Р": "R",
    "р": "r",
    "С": "S",
    "с": "s",
    "Т": "T",
    "т": "t",
    "У": "U",
    "у": "u",
    "Ф": "F",
    "ф": "f",
    "Х": "Kh",
    "х": "kh",
    "Ц": "Tc",
    "ц": "tc",
    "Ч": "Ch",
    "ч": "ch",
    "Ш": "Sh",
    "ш": "sh",
    "Щ": "Shch",
    "щ": "shch",
    "Ы": "Y",
    "ы": "y",
    "Э": "E",
    "э": "e",
    "Ю": "Iu",
    "ю": "iu",
    "Я": "Ia",
    "я": "ia",
}

with open('cyrillic.txt', 'r', encoding='utf-8') as rus:
    with open('transliteration.txt', 'w', encoding='utf-8') as eng:
        for i in rus.readlines():
            ans = ''
            for j in i:
                if j in let:
                    if j == 'ё':
                        ans += let['е']
                    elif j == 'Ё':
                        ans += let['Е']
                    else:
                        ans += let[j]
                elif j == 'ъ' or j == 'Ъ' or j == 'ь' or j == 'Ь':
                        continue
                else:
                    ans += j
            eng.write(ans)

                            