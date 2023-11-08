# А роза упала на лапу Азора 6.0
from sys import stdin

words = {w for w in stdin.read().split() if w.lower() == w.lower()[::-1]}
print(*sorted(words), sep='\n')
