# Разделяй и властвуй

data = []
with open(input(), 'r') as i:
    data = [line.split() for line in i.readlines()]

op = ['>', '<', '==']
for n in range(3):
    with open(input(), 'w') as o:
        for line in data:
            for i in line:
                if eval('len(list(filter(lambda x: not int(x) % 2, i)))'
                        + op[n] +
                        'len(list(filter(lambda x: int(x) % 2, i)))'):
                    print(i, end=' ', file=o)
            print('\n', end='', file=o)
