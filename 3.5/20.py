# Файловая сумма

with open('numbers.num', 'rb') as f:
    d = f.read()
    nums = [int.from_bytes(d[i:i + 2], 'big') for i in range(0, len(d), 2)]
    print(sum(nums) % 2 ** 16)
