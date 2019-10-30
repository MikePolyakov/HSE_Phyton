# Выборы Президента
'''
В выборах Президента Российской Федерации побеждает кандидат, набравший свыше
половины числа голосов избирателей. Если такого кандидата нет, то во второй тур
выборов выходят два кандидата, набравших наибольшее число голосов.

Формат ввода
Каждая строка входного файла содержит имя кандидата, за которого отдал голос
один избиратель. Известно, что общее число кандидатов не превосходит 20, но в
отличии от предыдущих задач список кандидатов явно не задан. Читайте данные из
файла input.txt с указанием кодировки utf8.

Формат вывода
Если есть кандидат, набравший более 50% голосов, программа должна вывести его
имя. Если такого кандидата нет, программа должна вывести имя кандидата,
занявшего первое место, затем имя кандидата, занявшего второе место.
Выводите данные в файл output.txt с указанием кодировки utf8.
'''
in_file = open("input.txt", encoding='utf8')
candidates = in_file.readlines()
in_file.close()

new_names = []
votes = 0
for name in candidates:
    name = name.strip()
    new_names.append(name)
    votes += 1

my_dict = dict()
for word in new_names:
    my_dict[word] = my_dict.get(word, 0) + 1

my_list = []
for key, value in my_dict.items():
    pair = (value, key)
    my_list.append(pair)

answer = sorted(my_list, reverse=True)

winner = answer[0][0]/votes

outFile = open('output.txt', 'w', encoding='utf8')
if winner > 0.5:
    print(answer[0][1], file=outFile)
else:
    print(answer[0][1], file=outFile)
    print(answer[1][1], file=outFile)

outFile.close()
