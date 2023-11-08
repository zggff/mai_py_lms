# Найдётся всё 2.0
from sys import stdin

lines = [ln.strip() for ln in stdin.readlines() if not ln.isspace()]
res = [ln for ln in lines[:-1] if lines[-1].lower() in ln.lower()]
print(*res, sep='\n')
