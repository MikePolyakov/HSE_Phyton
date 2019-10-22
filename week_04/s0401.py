# Минимум 4 чисел
'''
Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел,
которая не содержит инструкции if, а использует стандартную функцию min от
двух чисел. Считайте четыре целых числа и выведите их минимум.
'''


def min4(a, b, c, d):
    first = min(a, b)
    second = min(c, d)
    return min(first, second)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))
