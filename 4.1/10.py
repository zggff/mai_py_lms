# Слияние

def merge(a, b):
    res = []
    i = 0
    for v in a:
        while i < len(b) and b[i] <= v:
            res.append(b[i])
            i += 1
        res.append(v)
    while i < len(b):
        res.append(b[i])
        i += 1
    return tuple(res)
