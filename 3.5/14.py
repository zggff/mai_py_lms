# Слияние данных
import json

fname = input()
uname = input()

rec = []
ups = []
with open(fname, 'r') as f, open(uname, 'r') as f2:
    rec = json.load(f)
    ups = json.load(f2)

rec = {i['name']: {k: v for k, v in i.items() if k != 'name'} for i in rec}

for up in ups:
    if up['name'] in rec:
        for key in up:
            if key == 'name':
                continue
            if key not in rec[up['name']] or up[key] > rec[up['name']][key]:
                rec[up['name']][key] = up[key]

with open(fname, 'w') as f:
    json.dump(rec, f)
