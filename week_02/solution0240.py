# Максимальное число подряд идущих равных
'''
Дана последовательность натуральных чисел, завершающаяся числом 0.
Определите, какое наибольшее число подряд идущих элементов этой
последовательности равны друг другу.
'''
n = int(input())
element = n
maxElement = 1
finalAnswer = maxElement
while n != 0:
    n = int(input())
    if n != 0 and n == element:
        maxElement += 1
        if maxElement > finalAnswer:
            finalAnswer = maxElement
    elif n != 0 and n != element:
        maxElement = 1
        element = n
print(finalAnswer)
