# Самое частое слово
'''
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите то,
которое меньше в лексикографическом порядке.

Формат ввода
Вводится текст.
'''
in_file = open("input.txt", encoding='utf8')
text = in_file.read().split()
in_file.close()

myDict = dict()
for word in text:
    myDict[word] = myDict.get(word, 0) + 1
max_word_number = max(myDict.values())

answer = []
for key, value in myDict.items():
    if value == max_word_number:
        answer.append(key)
print(min(answer))
