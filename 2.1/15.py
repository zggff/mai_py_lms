N = int(input())
M = int(input())
T = int(input())

M += T
N += M // 60
M = M % 60
N = N % 24
print(f"{N:02}:{M:02}")
