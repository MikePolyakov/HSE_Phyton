# Количество слов в тексте
'''
Во входном файле (вы можете читать данные из sys.stdin,
подключив библиотеку sys) записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.

Формат ввода
Вводится текст.
'''
import sys
text = sys.stdin.readlines()
print(text)
# print(len(set(str(text.split(' ')))))
text_list = []
text_set = set()
for i in range(len(text)):
    text_list.append(text[i].split(' '))
    text_list[i][-1] = text_list[i][-1].strip()
    for j in range(len(text_list[i])):
        text_set.add(text_list[i][j])
print(len(text_set))
