# Переставить соседние
'''
Переставьте соседние элементы списка (A[0] c A[1],A[2] c A[3] и т.д.).
Если элементов нечетное число, то последний элемент остается на своем месте.
Вводится список чисел. Все числа списка находятся на одной строке.
'''
numList = list(map(int, input().split()))
if len(numList) % 2 == 0:
    for i in range(0, len(numList), 2):
        x = numList[i]
        numList[i] = numList[i+1]
        numList[i+1] = x
else:
    for i in range(0, len(numList)-1, 2):
        x = numList[i]
        numList[i] = numList[i+1]
        numList[i+1] = x
print(*numList)
