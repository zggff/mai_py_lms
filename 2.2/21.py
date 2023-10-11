x = float(input())
y = float(input())

if x ** 2 + y ** 2 > 10 ** 2:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
    exit()

if x >= 0 and y >= 0:
    zone = x ** 2 + y ** 2 <= 5 ** 2
elif y >= 0 and x >= -4:
    zone = y <= 5
elif y >= 0:
    zone = y <= 5 / 3 * (x + 7)
else:
    zone = y >= 0.25 * (x + 1) ** 2 - 9

if zone:
    print("Опасность! Покиньте зону как можно скорее!")
else:
    print("Зона безопасна. Продолжайте работу.")
