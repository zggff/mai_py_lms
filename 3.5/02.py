# Средний рост 
from sys import stdin

lines = [s := li.split() for li in stdin.readlines() if not li.isspace()]
res = round(sum([int(s[2]) - int(s[1]) for s in lines]) / len(lines))
print(res)
