available = set([input() for _ in range(int(input()))])
res = []
for _ in range(int(input())):
    name = input()
    valid = True
    for _ in range(int(input())):
        ingredient = input()
        if valid and ingredient not in available:
            valid = False
    if valid:
        res.append(name)
if len(res) == 0:
    print("Готовить нечего")
else:
    for r in sorted(res):
        print(r)
