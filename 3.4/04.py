import itertools

words = input().split()
for line in itertools.accumulate(words, lambda prev, x: prev + " " + x):
    print(line)
