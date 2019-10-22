# Последний максимум
'''
Найдите наибольшее значение в списке и индекс последнего элемента,
который имеет данное значение за один проход по списку,
не модифицируя этот список и не используя дополнительного списка.
Выведите два значения.
'''
numList = list(map(int, input().split()))
iMax = 0
element_max = numList[0]
for i in range(1, len(numList)):
    if numList[i] >= element_max:
        element_max = numList[i]
        iMax = i
print(element_max, iMax)
