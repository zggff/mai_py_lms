a = int(input())
b = int(input())
while (r := a % b) > 0:
    a = b
    b = r
print(b)
