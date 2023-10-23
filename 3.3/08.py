string = 'открытое акционерное общество'

res = ''.join([w[0].upper() for w in string.split()])

print(res)
