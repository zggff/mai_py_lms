rle = [('1', 1), ('0', 2), ('5', 1), ('0', 2)]

res = ''.join([a * i for a, i in rle])

print(res)
