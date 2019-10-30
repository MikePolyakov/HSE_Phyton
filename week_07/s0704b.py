# final result

inFile = open('input.txt', 'r', encoding='utf8')
text = inFile.readlines()
text_list = []
text_set = set()
for i in range(len(text)):
    text_list.append(text[i].split(' '))
    text_list[i][-1] = text_list[i][-1].strip()
    for j in range(len(text_list[i])):
        text_set.add(text_list[i][j])
text_set.discard('')
print(len(text_set))
