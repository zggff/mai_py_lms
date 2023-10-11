r = {
    int(input()): "Петя",
    int(input()): "Вася",
    int(input()): "Толя"
}
i = 1
for k in sorted(r.keys(), reverse=True):
    print(f"{i}. {r[k]}")
    i += 1
