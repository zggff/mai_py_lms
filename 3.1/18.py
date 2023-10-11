s = input()

prev = s[0]
cnt = 1
for c in s[1:]:
    if c != prev:
        print(prev, cnt)
        prev = c
        cnt = 1
    else:
        cnt += 1
print(prev, cnt)
