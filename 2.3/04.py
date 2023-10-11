a = int(input())
b = int(input())
if b >= a:
    res = range(a, b + 1)
else:
    res = range(a, b - 1, -1)
print(*res, sep=' ')
