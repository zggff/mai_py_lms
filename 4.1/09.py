# Простая задача 5.0

def is_prime(n: int) -> bool:
    for dl in range(2, int(n ** 0.5) + 1):
        if n % dl == 0:
            return False
    return True
