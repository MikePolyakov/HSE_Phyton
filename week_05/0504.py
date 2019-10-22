def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    hand_copy = hand.copy()
    if word in wordList:
        for element in word:
            if element in hand_copy:
                hand_copy[element] -= 1
                if hand_copy[element] == 0:
                    del (hand_copy[element])
            else:
                return False
                break
        return True
    else:
        return False


filename = 'words.txt'
wordList = []
file = open(filename).read().split('\n')
for line in file:
    wordList.append(line.lower())
'''
with open(filename) as file:
    for line in file:
        if upper_word in line and len(upper_word) == (len(line) - 1):
            print('Yes', line)
'''
hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
word = "hello"
print(isValidWord(word, hand, wordList))

hand = {'n': 1, 'b': 1, 'o': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}
word = "honey"
print(isValidWord(word, hand, wordList))

hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
word = "quail"
print(isValidWord(word, hand, wordList))

hand = {'b':1, 'v':2, 'n':1, 'i':1, 'l':2}
word = "evil"
print(isValidWord(word, hand, wordList))
