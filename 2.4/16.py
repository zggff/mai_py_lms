N = int(input())
size = int(input())
row_len = size * N + (N - 1)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        n = f'{i * j}'
        s = len(n)
        b = (size - s) // 2
        a = (size + 1 - s) // 2
        print(' ' * b + n + ' ' * a, end='')
        if j < N:
            print('|', end='')
    print()
    if i < N:
        print('-' * row_len)
