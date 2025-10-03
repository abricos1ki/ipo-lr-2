import math
a = float(input('Введие значение нижнего основания ' ' '))
b = float(input('Введие значение верхнего основания ' ' '))
c = float(input('Введие значение правой стороны ' ' '))
d = float(input('Введие значение левой  стороны ' ' '))
p = ( (a + b + c + d ) / 2)
S = ((a + b) / abs(a - b)) * math.sqrt( (p - a) * (p - b) * (p - a - c) * (p - a - d))
print(S)