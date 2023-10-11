n = int(input())
result = all([input()[0].lower() in "абв" for _ in range(n)])

print("YES" if result else "NO")
