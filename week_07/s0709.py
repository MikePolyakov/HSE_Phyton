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

words_dict = dict()
min_entry = 1
min_word = text[0]
for word in text:
    words_dict[word.strip()] = words_dict.get(word.strip(), 0) + 1
    if int(words_dict[word.strip()]) >= min_entry:
        if word.strip() < min_word:
            min_entry = int(words_dict[word.strip()])
            min_word = word.strip()

print(min_word)


fin = open('input.txt', encoding='utf8')
d = {}
for line in fin:
    words = line.strip().split()
    for word in words:
        d[word] = d.get(word, 0) + 1
print(sorted(d.items(), key=lambda x: (-x[1], x[0]))[0][0])

wordS = (str(sys.stdin.read()).split())
myDict = {}
for word in wordS:
    myDict[word] = myDict.get(word, 0) + 1
maxW = max(myDict.values())
print(min(list(a for a, b in myDict.items() if b == maxW)))
lst = []
for a, b in myDict.items():
    if b == maxW:
        lst.append(a)
print(min(lst))

