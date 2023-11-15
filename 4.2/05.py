# Подготовка данных

def to_string(*data, sep=' ', end='\n'):
    return sep.join(map(str, data)) + end
