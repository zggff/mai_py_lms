# Файловая чистка

with open(input(), 'r') as i, open(input(), 'w') as o:
    for ln in i:
        words = ' '.join([w for w in ln.replace(
            '\t', '').split() if not w.isspace()])
        if words == '':
            continue
        print(words, file=o)
