# Рекурсивный сумматор цифр

def recursive_digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + recursive_digit_sum(n // 10)
