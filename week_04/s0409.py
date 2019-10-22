# Сократите дробь
'''
Даны два натуральных числа n и m.
Сократите дробь (n / m), то есть выведите два других числа p и q таких,
что (n / m) = (p / q) и дробь (p / q) — несократимая.
Решение оформите в виде функции ReduceFraction(n, m),
получающая значения n и m и возвращающей кортеж из двух чисел: return p, q.
Тогда вывод можно будет оформить как print(*ReduceFraction(n, m)).
'''


def ReduceFraction(n, m):
    k = gcd(n, m)
    return n // k, m // k


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
