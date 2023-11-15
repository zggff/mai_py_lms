# Многочлен N-ой степени

def make_equation(*args):
    if len(args) == 1:
        return str(args[0])
    return (
        '(' +
        make_equation(*args[:-1]) +
        ') * x ' +
        ('- ' if args[-1] < 0 else '+ ') +
        str(args[-1])
    )
