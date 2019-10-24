# Сортировка подсчетом
'''
Дан список из N (N≤2*10⁵) элементов,
которые принимают целые значения от 0 до 100.

Отсортируйте этот список в порядке неубывания элементов.
Выведите полученный список.

Решение оформите в виде функции CountSort(A),
которая модифицирует передаваемый ей список.
Использовать встроенные функции сортировки нельзя.
'''


def CountSort(A):
    cntMarks = [0] * 101
    for element in A:
        cntMarks[element] += 1
    B = ''
    for nowMark in range(101):
        new_element = (str(nowMark) + ' ') * cntMarks[nowMark]
        B += new_element
    return B


input_list = map(int, input().split())
print(CountSort(input_list))
