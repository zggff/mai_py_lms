x = 0
y = 0

while (dir := input()) != "СТОП":
    steps = int(input())
    match dir:
        case "СЕВЕР": y += steps
        case "ЮГ": y -= steps
        case "ВОСТОК": x += steps
        case "ЗАПАД": x -= steps
print(y)
print(x)
