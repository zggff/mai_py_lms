N = int(input())
M = int(input())

s = 1
n_len = len(str(N * M))
table = []
for i in range(M):
    row = []
    for j in range(N):
        n = s - j if i % 2 else s + j
        row.append(f"{n:{n_len}}")
    if i % 2:
        s += 1
    else:
        s += N * 2 - 1
    table.append(row)

for i in range(N):
    for j in range(M):
        print(table[j][i], end=' ')
    print()
