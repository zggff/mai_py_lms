name = input()
price = int(input())
weight = int(input())
money = int(input())
total = price * weight
rem = money - total

print(f"{'='*16}Чек{'='*16}")
print(f"Товар:{' '*(29-len(name))}{name}")
print(
    f"Цена:{' '*(19-len(str(price)) - len(str(weight)))}{weight}кг * {price}руб/кг")
print(f"Итого:{' '*(26-len(str(total)))}{total}руб")
print(f"Внесено:{' '*(24-len(str(money)))}{money}руб")
print(f"Сдача:{' '*(26-len(str(rem)))}{rem}руб")
print(f"{'='*35}")
