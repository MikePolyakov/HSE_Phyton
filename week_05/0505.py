def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    number_of_letters = 0
    for letter in hand:
        number_of_letters += hand[letter]
    return number_of_letters


hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
print(calculateHandlen(hand))

hand = {'v':1, 'n':1, 'l':1}
print(calculateHandlen(hand))
