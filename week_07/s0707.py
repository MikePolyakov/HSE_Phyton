# Номер появления слова
'''
Во входном файле (вы можете читать данные из файла input.txt) записан текст.
Словом считается последовательность непробельных подряд идущих символов.
Слова разделены одним или большим числом пробелов или символами конца строки.
Для каждого слова из этого текста подсчитайте,
сколько раз оно встречалось в этом тексте ранее.

Формат ввода
Вводится текст.

inFile = open('input.txt', 'r', encoding='utf8')
in_text = inFile.readlines()
inFile.close()
'''
in_text = input()
print(in_text, 'len=', len(in_text))
text_01 = []
text_02 = []
for i in range(len(in_text)):
    text_01.append(in_text[i].split(' '))
    text_01[i][-1] = text_01[i][-1].strip()
    print(text_01)
    for j in range(len(text_01[i])):
        text_02.append(text_01[i][j])
        print(text_02)
words = dict()
for element in text_02:
    words[element] = words.get(element, 0) + 1

    print(words[element] - 1, end=' ')


'''
fin = open("input.txt")
myDict = {}
checker = list()
# Нарезать строку на слова
for line in fin:
    words = line.split(" ")
    i = 0  # считает вхождения слов
    for word in words:
        if word not in myDict:
            myDict[word.strip()] = 1
            checker.append(0)
        else:
            myDict[word.strip()] = myDict[word.strip()] + 1
            checker.append(myDict[word.strip()] - 1)
print(*checker, "")
'''

'''
file = file.read().split()
line.strip().split()

'''