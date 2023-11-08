# Файловая статистика 2.0
import json

with open(input(), 'r') as f, open(input(), 'w') as o:
    ns = [int(i) for i in f.read().split()]
    rec = {'count': len(ns),
           'positive_count': len([n for n in ns if n > 0]),
           'min': min(ns),
           'max': max(ns),
           'sum': sum(ns),
           'average': round(sum(ns) / len(ns), 2)
           }
    json.dump(rec, o)
