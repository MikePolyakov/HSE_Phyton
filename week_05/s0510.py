# Количество положительных
'''
Найдите количество положительных элементов в данном списке.

Вводится список чисел. Все числа списка находятся на одной строке.
'''
numList = list(map(int, input().split()))
iCount = 0
for i in range(len(numList)):
    if numList[i] > 0:
        iCount += 1
print(iCount)
