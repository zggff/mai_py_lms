# "Выпрямление" списка

def make_linear(arr):
    res = []
    for v in arr:
        if isinstance(v, list):
            res.extend(make_linear(v))
        else:
            res.append(v)
    return res
