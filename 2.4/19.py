N = int(input())
s = len(str((N + 1) // 2))
table = []
for i in range(1, (N + 1) // 2 + 1):
    line = []
    for j in range(1, (N + 1) // 2 + 1):
        line.append(min(i, j))
    line += line[-1 - N % 2::-1]
    table.append(line)
table += table[-1 - N % 2::-1]
for line in table:
    for val in line:
        print(f"{val:{s}}", end=" ")
    print()
