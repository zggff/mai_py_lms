def make_matrix(size, value=0):
    if isinstance(size, int):
        x, y = size, size
    else:
        x, y = size
    return [[value] * x for _ in range(y)]
