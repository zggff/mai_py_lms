# Найдётся всё 3.0
from sys import stdin

lines = [line.strip() for line in stdin.readlines()]
query = ' '.join([w.lower() for w in lines[0].split()])
found = False
for fname in lines[1:]:
    with open(fname, 'r') as f:
        cont = ' '.join(f.read().lower().split())
        if query in cont:
            found = True
            print(fname)
if not found:
    print('404. Not Found')
