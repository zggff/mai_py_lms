a = int(input())
b = int(input())
r = a
while r % b != 0:
    r += a
print(r)
