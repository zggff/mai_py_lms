n = int(input())
lines = []
i = 1
j = 1
size = 0
while i <= n:
    line = ""
    for _ in range(j):
        if i > n:
            break
        line += str(i) + " "
        i += 1
    line = line.strip()
    lines.append(line)
    size = max(size, len(line))
    j += 1
for line in lines:
    s = len(line)
    b = (size - s) // 2
    a = (size + 1 - s) // 2
    print(" " * b + line + " " * a)
