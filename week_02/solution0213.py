# Тип треугольника
'''
Даны три стороны треугольника a,b,c.
Определите тип треугольника с заданными сторонами.
Выведите одно из четырех слов: rectangular для прямоугольного треугольника,
acute для остроугольного треугольника,
obtuse для тупоугольного треугольника
или impossible, если треугольника с такими сторонами не существует
(считаем, что вырожденный треугольник тоже невозможен).
'''
x1 = int(input())
x2 = int(input())
x3 = int(input())
if x1 <= x2 <= x3:
    b = x1
    a = x2
    c = x3
elif x2 <= x1 <= x3:
    b = x2
    a = x1
    c = x3
elif x2 <= x3 <= x1:
    b = x2
    a = x3
    c = x1
elif x3 <= x2 <= x1:
    b = x3
    a = x2
    c = x1
elif x3 <= x1 <= x2:
    b = x3
    a = x1
    c = x2
elif x1 <= x3 <= x2:
    b = x1
    a = x3
    c = x2
if (a + b) > c > (a - b):
    if c ** 2 == (a ** 2 + b ** 2):
        print('rectangular')
    elif c ** 2 < (a ** 2 + b ** 2):
        print('acute')
    elif c ** 2 > (a ** 2 + b ** 2):
        print('obtuse')
else:
    print('impossible')
