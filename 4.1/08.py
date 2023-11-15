# А роза упала на лапу Азора 7.0

def is_palindrome(v: int) -> bool:
    if isinstance(v, int):
        return str(v) == str(v)[::-1]
    return v == v[::-1]
