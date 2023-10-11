N = int(input())
M = int(input())
s = len(str(N * M))
n = 1
for _ in range(N):
    for _ in range(M):
        print(f"{n:{s}}", end=' ')
        n += 1
    print()
