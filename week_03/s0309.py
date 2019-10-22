# Система линейных уравнений - 1
'''
Даны вещественные числа a, b, c, d, e, f.
Известно, что система линейных уравнений:
ax + by = e
cx + dy = f
имеет ровно одно решение.
Выведите два числа x и y, являющиеся решением этой системы.
x=(de-fb)/(da-bc)
y=(fa-ec)/(da-bc)
'''
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
x = (d * e - f * b)/(d * a - b * c)
y = (f * a - e * c)/(d * a - b * c)
print(x, y)
