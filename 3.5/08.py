# Файловая разница

with (open(input(), 'r') as i1,
      open(input(), 'r') as i2, open(input(), 'w') as o):
    w1 = set(i1.read().split())
    w2 = set(i2.read().split())
    o.write('\n'.join(sorted(w1 ^ w2)))
