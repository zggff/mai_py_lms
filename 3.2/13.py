n = int(input())
available = set([input() for _ in range(n)])
m = int(input())
done = set()
for _ in range(m):
    k = int(input())
    for _ in range(k):
        done.add(input())
res = available - done
if len(res) == 0:
    print("Готовить нечего")
else:
    for r in sorted(res):
        print(r)
