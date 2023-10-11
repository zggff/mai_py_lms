year = int(input())
res = False

if year % 100 == 0:
    res = year % 400 == 0
else:
    res = year % 4 == 0
if res:
    print("YES")
else:
    print("NO")
