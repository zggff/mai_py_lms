N = int(input())
t = 3
for i in range(1, N + 1):
    for j in range(t, 0, -1):
        print(f"До старта {j} секунд(ы)")
    t += 1
    print(f"Старт {i}!!!")
