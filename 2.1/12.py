a = [int(i) for i in input()][::-1]
b = [int(i) for i in input()][::-1]
res = []
for i in range(min(len(a), len(b))):
    res.append((a[i] + b[i]) % 10)
if len(a) > len(b):
    res += a[len(b):]
if len(b) > len(a):
    res += b[len(a):]
print(''.join(map(str, reversed(res))))
