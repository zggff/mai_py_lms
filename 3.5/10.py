# Хвост

with open(input(), 'r') as i:
    res = i.readlines()[-int(input()):]
    print(*res, sep='', end='')
