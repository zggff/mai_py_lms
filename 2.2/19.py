s = sorted([int(input()), int(input()), int(input())])

a = s[0] ** 2
b = s[1] ** 2
c = s[2] ** 2

if a + b > c:
    print("крайне мала")
elif a + b == c:
    print("100%")
else:
    print("велика")
