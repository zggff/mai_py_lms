# Кофейня

def order(*args):
    global in_stock
    for order in args:
        match order:
            case "Эспрессо":
                if in_stock["coffee"] >= 1:
                    in_stock["coffee"] -= 1
                    return order
            case "Капучино":
                if in_stock["coffee"] >= 1 and in_stock["milk"] >= 3:
                    in_stock["coffee"] -= 1
                    in_stock["milk"] -= 3
                    return order
            case "Макиато":
                if in_stock["coffee"] >= 2 and in_stock["milk"] >= 1:
                    in_stock["coffee"] -= 2
                    in_stock["milk"] -= 1
                    return order
            case "Кофе по-венски":
                if in_stock["coffee"] >= 1 and in_stock["cream"] >= 2:
                    in_stock["coffee"] -= 1
                    in_stock["cream"] -= 2
                    return order
            case "Латте Макиато":
                if (in_stock["coffee"] >= 1
                        and in_stock["milk"] >= 2 and in_stock["cream"] >= 1):
                    in_stock["coffee"] -= 1
                    in_stock["milk"] -= 2
                    in_stock["cream"] -= 1
                    return order
            case "Кон Панна":
                if in_stock["coffee"] >= 1 and in_stock["cream"] >= 1:
                    in_stock["coffee"] -= 1
                    in_stock["cream"] -= 1
                    return order
    return "К сожалению, не можем предложить Вам напиток"
