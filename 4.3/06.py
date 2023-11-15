# Сортировка слиянием

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = int(len(arr) / 2)
    return merge(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


def merge(a, b):
    res = []
    i = 0
    for v in a:
        while i < len(b) and b[i] <= v:
            res.append(b[i])
            i += 1
        res.append(v)
    while i < len(b):
        res.append(b[i])
        i += 1
    return res


result = merge_sort([3, 1, 5])
print(result)
