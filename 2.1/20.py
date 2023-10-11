N = int(input())
M = int(input())
k1 = int(input())
k2 = int(input())

# for m in range(1, N):
#     if m * k1 + (N - m) * k2 == N * M:
#         print(m, N-m)
#         break
#
m = N * (M - k2) // (k1 - k2)
print(m, N - m)
