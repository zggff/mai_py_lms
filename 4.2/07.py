# В эфире рубрика «Эксперименты»

results = []


def enter_results(*args):
    global results
    results.extend(args)


def get_sum():
    global results
    a, b = 0, 0
    for i in range(0, len(results), 2):
        a += results[i]
        b += results[i + 1]
    return (a, b)


def get_average():
    global results
    a, b = 0, 0
    cnt = len(results) // 2
    for i in range(0, len(results), 2):
        a += results[i]
        b += results[i + 1]
    return (a / cnt, b / cnt)
