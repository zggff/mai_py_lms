# Модернизация системы вывода
printed = set()


def modern_print(s: str):
    global printed
    if s not in printed:
        print(s)
        printed.add(s)
