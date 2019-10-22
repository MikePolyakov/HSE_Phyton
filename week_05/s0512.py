# Больше предыдущего
'''
Дан список чисел. Выведите все элементы списка,
которые больше предыдущего элемента.

Вводится список чисел. Все числа списка находятся на одной строке.
'''
numList = list(map(int, input().split()))
for i in range(1, len(numList)):
    if numList[i] > numList[i - 1]:
        print(numList[i], sep=' ', end=' ')
