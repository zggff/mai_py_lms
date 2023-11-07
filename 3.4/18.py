# Таблица истинности
import itertools as it

expr = input()
print("a b c f")
for a, b, c in it.product(range(2), repeat=3):
    f = eval(expr) * 1
    print(f"{a} {b} {c} {f}")
