data = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
for i in range(int(input())):
    print(data[i % 5])
