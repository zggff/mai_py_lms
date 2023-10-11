n = int(input())
print("А Б В")
for a in range(1, n):
    for b in range(1, n):
        if a + b >= n:
            break
        print(f"{a} {b} {n - a - b}")
