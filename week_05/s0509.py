# Четные элементы
'''
Выведите все четные элементы списка.
Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.
'''
numList = list(map(int, input().split()))
for i in range(len(numList)):
    if numList[i] % 2 == 0:
        print(numList[i], sep=' ', end=' ')
