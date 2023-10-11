N = int(input())
M = int(input())

s = 1
n_len = len(str(N * M))
for i in range(N):
    for j in range(M):
        n = s - j if i % 2 else s + j
        print(f"{n:{n_len}}", end=' ')
    if i % 2:
        s += 1
    else:
        s += M * 2 - 1
    print()
