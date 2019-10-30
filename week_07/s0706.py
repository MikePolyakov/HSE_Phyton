# Полиглоты
'''
Каждый из N школьников некоторой школы знает Mᵢ языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.

Формат ввода
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mᵢ, после каждого из чисел идет Mᵢ строк,
содержащих названия языков, которые знает i-й школьник. Длина названий языков
не превышает 1000 символов,
количество различных языков не более 1000. 1≤N≤1000, 1≤Mᵢ≤500.

Формат вывода
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков. Затем - количество языков,
которые знает хотя бы один школьник, на следующих строках - список таких языков
'''
n = int(input())
all_languages = set()
for i in range(n):
    m = int(input())
    i_set = set()
    for j in range(m):
        input_line = input()
        if input_line not in all_languages:
            all_languages.add(input_line)
        i_set.add(input_line)
    if i == 0:
        one_for_all = i_set
    else:
        one_for_all &= i_set
print(len(one_for_all))
for element in one_for_all:
    print(element)
print(len(all_languages))
for element in all_languages:
    print(element)
