# Файловая статистика

with open(input(), 'r') as f:
    ns = [int(i) for i in f.read().split()]
    print(len(ns))
    print(len([n for n in ns if n > 0]))
    print(min(ns))
    print(max(ns))
    print(sum(ns))
    print(f"{sum(ns)/len(ns):0.2f}")
