N = int(input())
M = int(input())
s = len(str(N * M))
i = 1
for _ in range(N):
    n = i
    for _ in range(M):
        print(f"{n:{s}}", end=' ')
        n += N
    i += 1
    print()
