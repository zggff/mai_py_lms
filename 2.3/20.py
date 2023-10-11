N = int(input())
h_prev = 0

for i in range(N):
    b = int(input())
    h = b & 0xFF
    r = (b & 0xFF << 8) >> 8
    m = (b & 0xFF << 16) >> 16
    h_correct = (37 * (m + r + h_prev)) % 256
    h_prev = h
    if h != h_correct or h_correct >= 100 or h >= 100:
        print(i)
        exit()
print(-1)
