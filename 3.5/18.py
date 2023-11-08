import os
import math

size = (os.path.getsize(input()), 'Б')
if size[0] >= 1024:
    size = (math.ceil(size[0] / 1024), 'КБ')
if size[0] >= 1024:
    size = (math.ceil(size[0] / 1024), 'МБ')
if size[0] >= 1024:
    size = (math.ceil(size[0] / 1024), 'ГБ')

print(f'{size[0]}{size[1]}')



