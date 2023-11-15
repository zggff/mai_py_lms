# Функциональный нод 2.0

def gcd(*args):
    a = list(args)
    while len(a) > 1:
        while a[0] > 0:
            a[1], a[0] = a[0], a[1] % a[0]
        a.pop(0)
    return a[0]
