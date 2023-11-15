# Накопление результата
def result_accumulator(f):
    result = []

    def decorated(*args, method='accumulate'):
        result.append(f(*args))
        if method == 'drop':
            res = result.copy()
            result.clear()
            return res
    return decorated
