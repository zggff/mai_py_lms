numbers = [1, 2, 3, 4, 5]
numbers = [number for number in range(16, 100, 4)]

res = {i for i in numbers if any([j * j == i for j in range(1, i + 1)])}

print(res)
