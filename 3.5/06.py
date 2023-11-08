# Транслитерация 2.0
code = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "Zh",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "Kh",
    "Ц": "Tc",
    "Ч": "Ch",
    "Ш": "Sh",
    "Щ": "Shch",
    "Ы": "Y",
    "Э": "E",
    "Ю": "Iu",
    "Я": "Ia",
    "Ё": "E",
    "Й": "I",
    "Ь": "",
    "Ъ": ""
}

with open('cyrillic.txt') as i, open('transliteration.txt', 'w') as o:
    res = ""
    for char in i.read():
        if char.upper() in code:
            if char.isupper():
                res += code[char]
            else:
                res += code[char.upper()].lower()
        else:
            res += char
    o.write(res)
