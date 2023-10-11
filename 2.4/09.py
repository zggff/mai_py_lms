N = int(input())
r = ""
for _ in range(N):
    m = '0'
    for i in input():
        m = max(m, i)
    r += m
print(r)
