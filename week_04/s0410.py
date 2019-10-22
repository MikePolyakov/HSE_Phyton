# Сумма последовательности
'''
Дана последовательность чисел, завершающаяся числом 0.
Найдите сумму всех этих чисел, не используя цикл.
'''


def elements_sum():
    n = int(input())
    if n == 0:
        return 0
    else:
        return n + elements_sum()


print(elements_sum())
