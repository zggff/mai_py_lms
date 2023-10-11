a = [int(i) for i in input()]
b = [int(i) for i in input()]
c = sorted(a + b, reverse=True)
print(''.join(map(str, [c[0], (c[1] + c[2]) % 10, c[3]])))
