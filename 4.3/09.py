# Циклический генератор

def cycle(arr):
    i = 0
    while True:
        yield arr[i]
        i = (i + 1) % len(arr)
