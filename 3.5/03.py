# Без комментариев 2.0
from sys import stdin

lines = [line[0:line.find('#')] for line in stdin.readlines()]
lines = [line for line in lines if line != '']
print(*lines, sep='\n')
