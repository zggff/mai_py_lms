# Сколько вешать в байтах?
import os

size = os.path.getsize(input())
if size > 1024**3 - 1:
    size = int(size / 1024**3) + 1
    unit = 'ГБ'
elif size > 1024**2 - 1:
    size = int(size / 1024**2) + 1
    unit = 'МБ'
elif size > 1023:
    size = int(size / 1024) + 1
    unit = 'КБ'
else:
    unit = 'Б'
print(str(size) + unit)
