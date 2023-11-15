# Однотипность не порок

def same_type(func):
    def decorated(*args):
        if len(set(map(type, args))) != 1:
            print("Обнаружены различные типы данных")
            return False
        return func(*args)

    return decorated
