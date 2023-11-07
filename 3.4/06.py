import itertools as it

vals = it.chain(map(str, range(2, 10 + 1)), ["валет", "дама", "король", "туз"])
typee = ["пик", "треф", "бубен", "червей"]
typee.remove(input())
for a, b in it.product(vals, typee):
    print(a, b)
