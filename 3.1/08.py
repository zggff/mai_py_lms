n = int(input())

for _ in range(n):
    i = input().find("зайка")
    if i == -1:
        print("Заек нет =(")
    else:
        print(i + 1)
