import math
V = float(input('Дан объем шара (куб. ед):' ))
r = (3 * V / (4 * math.pi)) ** (1 / 3)
print (f'Радиус шара: {r} ед.')