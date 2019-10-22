# Наименьший положительный
'''
Выведите значение наименьшего из всех положительных элементов в списке.
Известно, что в списке есть хотя бы один положительный элемент,
а значения всех элементов списка по модулю не превосходят 1000.

Вводится список чисел. Все числа списка находятся на одной строке.
'''
numList = list(map(int, input().split()))
newList = []
for i in range(len(numList)):
    if numList[i] > 0:
        newList.append(numList[i])
element = newList[0]
for i in range(1, len(newList)):
    if newList[i] < element:
        element = newList[i]
print(element)
