# Обновление данных
import json
from sys import stdin

lines = stdin.readlines()

f = open(lines[0].strip(), 'r')
rec = json.load(f)
f.close()

f = open(lines[0].strip(), 'w')
for line in lines[1:]:
    key, value = line.split('==')
    rec[key.strip()] = value.strip()
json.dump(rec, f)
f.close()
