# А есть ещё варианты?
import itertools as it

incl = input()
excl = input()
prev = input()

suit = {
    'буби': 'бубен',
    'пики': 'пик',
    'трефы': 'треф',
    'черви': 'червей',
}
val = ["10", *[str(i) for i in range(2, 10)], 'валет', 'дама', 'король', 'туз']
combs = it.starmap(lambda a, b: f'{a} {b}', it.product(val, suit.values()))
res = [a for a in it.combinations(combs, 3)
       if any((suit[incl] in i for i in a))
       and all(excl not in i for i in a)]
res = [', '.join(r) for r in res]
print(res[res.index(prev) + 1])
