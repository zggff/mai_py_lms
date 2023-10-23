text = 'Мама мыла раму!'

res = {x: text.lower().count(x) for x in text.lower() if x.isalpha()}
print(res)
