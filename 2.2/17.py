r = {
    int(input()): "Петя",
    int(input()): "Вася",
    int(input()): "Толя"
}
res = [r[i] for i in sorted(r.keys(), reverse=True)]
print(" " * 10 + res[0] + " " * 10)
print(" " * 2 + res[1] + " " * 18)
print(" " * 18 + res[2] + " " * 2)
print(" " * 3 + "II" + " " * 6 +
      "I" + " " * 6 + "III" + " " * 3)
