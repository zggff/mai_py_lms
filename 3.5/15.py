# Поставь себя на моё место
import json

scoring = []
with open('scoring.json') as f:
    scoring = json.load(f)


res = 0
for tests in scoring:
    ppt = tests['points'] // len(tests['tests'])
    for test in tests['tests']:
        if input() == test['pattern']:
            res += ppt
print(res)
