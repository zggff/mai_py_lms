numbers = {1, 2, 3, 4, 5}

res = {n: [i for i in range(1, n + 1) if n % i == 0] for n in numbers}

print(res)
