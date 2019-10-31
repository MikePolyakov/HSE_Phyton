# Произведение пятых степеней
'''
На вход подаётся последовательность натуральных чисел длины n≤1000.
Посчитайте произведение пятых степеней чисел в последовательности.

Для решения задачи используйте функцию reduce из модуля functools
reduce(function, iterable[, initializer])
'''
from functools import reduce


numList = list(map(int, input().split()))
print(numList)
print(reduce(lambda x, y: x*(y**5), numList, 1))

# initializing list
# lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
# print("The sum of the list elements is : ", end="")
# print(functools.reduce(lambda a, b: a + b, lis))

# using reduce to compute maximum element from list
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))
