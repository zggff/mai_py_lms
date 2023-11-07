n = int(input())
m = int(input())
m_len = len(str(m * n))

for r in range(1, m * n + 1):
    print(f"{r:>{m_len}}", end=" ")
    if r % m == 0:
        print()
