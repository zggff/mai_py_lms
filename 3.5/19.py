# Это будет наш секрет

a = ''.join([chr(c) for c in range(ord('a'), ord('z') + 1)])
shift = int(input())
with open('public.txt', 'r') as i, open('private.txt', 'w') as o:
    text = ''
    for c in i.read():
        if c.lower() not in a:
            text += c
            continue
        c2 = a[(a.find(c.lower()) + shift) % len(a)]
        if c.isupper():
            text += c2.upper()
        else:
            text += c2
    o.write(''.join(text))
