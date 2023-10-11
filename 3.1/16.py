s_len = int(input())
s_cnt = int(input())
ss = [input() for _ in range(s_cnt)]

for s in ss:
    if len(s) >= s_len - 3:
        print(s[:s_len - 3] + '...')
        break
    print(s)
    s_len -= len(s)
