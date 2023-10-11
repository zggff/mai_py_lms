petya = int(input())
vasya = int(input())
tolya = int(input())
if max(petya, vasya, tolya) == petya:
    print("Петя")
elif max(petya, vasya, tolya) == vasya:
    print("Вася")
else:
    print("Толя")
