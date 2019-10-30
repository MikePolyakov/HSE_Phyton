in_file = open("input.txt")
text = in_file.read().split()
in_file.close()
words_dict = dict()
answer = []
for word in text:
    words_dict[word.strip()] = words_dict.get(word.strip(), 0) + 1
    answer.append(words_dict[word.strip()] - 1)
print(*answer)
