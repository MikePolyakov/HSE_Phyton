# Переставить min и max
'''
В списке все элементы попарно различны.
Поменяйте местами минимальный и максимальный элемент этого списка.

Вводится список целых чисел. Все числа списка находятся на одной строке.
'''
numList = list(map(int, input().split()))
iMax = 0
element_max = numList[0]
for i in range(1, len(numList)):
    if numList[i] >= element_max:
        element_max = numList[i]
        iMax = i
iMin = 0
element_min = numList[0]
for i in range(1, len(numList)):
    if numList[i] <= element_min:
        element_min = numList[i]
        iMin = i
x = numList[iMin]
numList[iMin] = numList[iMax]
numList[iMax] = x
print(*numList)
