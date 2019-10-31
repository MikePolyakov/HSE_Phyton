# Количество различных чисел
'''
Дан список чисел, который может содержать до 100000 чисел.Определите,
сколько в нем встречается различных чисел.

Формат ввода
Вводится список целых чисел. Все числа списка находятся на одной строке.
'''

in_file = open("input.txt")
numbers = in_file.read().split()
in_file.close()
my_dict = dict()
for number in numbers:
    my_dict[number] = my_dict.get(number, 0) + 1
print(len(my_dict))
