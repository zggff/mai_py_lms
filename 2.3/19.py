a = 1
b = 1000
while True:
    m = (a + b) // 2
    print(m)
    r = input()
    match r:
        case "Меньше": b = m - 1
        case "Больше": a = m + 1
        case "Угадал!": exit()
