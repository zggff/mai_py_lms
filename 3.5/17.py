# Прятки

with open('secret.txt', 'r') as f:
    res = ''
    for byte in f.read():
        if ord(byte) < 128:
            res += byte
        else:
            res += chr(ord(byte) & 0xff)
    print(res)
