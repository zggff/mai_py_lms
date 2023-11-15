# Ключевой секрет

def secret_replace(text, **kwargs):
    r = ''
    rules = {d: v for d, v in kwargs.items()}
    lens = {d: len(v) for d, v in kwargs.items()}
    offset = {d: 0 for d, _ in kwargs.items()}
    for c in text:
        if c in rules:
            r += rules[c][offset[c]]
            offset[c] = (offset[c] + 1) % lens[c]
        else:
            r += c
    return r
