# Таблица истинности 2
import itertools as it

expr = input()
vars = sorted({a for a in expr if a.isupper()})
print(*vars, "F")
for p in it.product(range(2), repeat=len(vars)):
    print(*p, eval(expr, {}, {s: p[i] for i, s in enumerate(vars, 0)}) * 1)
