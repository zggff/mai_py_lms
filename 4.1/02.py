# Функциональный НОД

def gcd(a: int, b: int) -> int:
    while (r := a % b) > 0:
        a = b
        b = r
    return b
