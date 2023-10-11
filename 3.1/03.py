s_len = int(input())
s_cnt = int(input())

for _ in range(s_cnt):
    s = input()
    if len(s) <= s_len:
        print(s)
    else:
        print(s[:s_len - 3], end='...\n')
