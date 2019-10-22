# Слияние списков
"""
Даны два целочисленных списка A и B, упорядоченных по неубыванию.
Объедините их в один упорядоченный список С
(то есть он должен содержать len(A)+len(B) элементов).
Решение оформите в виде функции merge(A, B), возвращающей новый список.
Алгоритм должен иметь сложность O(len(A)+len(B)).
Модифицировать исходные списки запрещается.
Использовать функцию sorted и метод sort запрещается.

Программа получает на вход два неубывающих списка, каждый в отдельной строке.
"""


def merge(A, B):
    first_list = A.copy()
    second_list = B.copy()
    C = []
    while len(first_list) > 0 and len(second_list) > 0:
        if first_list[0] <= second_list[0]:
            C.append(first_list[0])
            first_list.remove(first_list[0])
        else:
            C.append(second_list[0])
            second_list.remove(second_list[0])
    if len(first_list) < len(second_list):
        C.extend(second_list)
    else:
        C.extend(first_list)
    return C


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = merge(a, b)
print(*c)
