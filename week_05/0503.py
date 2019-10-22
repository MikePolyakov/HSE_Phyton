def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    hand_copy = hand.copy()
    for element in word:
        if element in hand_copy:
            hand_copy[element] -= 1
            if hand_copy[element] == 0:
                del(hand_copy[element])
    return hand_copy


hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
hand2 = updateHand(hand, 'quail')
print(hand)
print(hand2)

hand = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
hand3 = updateHand(hand, 'evil')
print(hand)
print(hand3)

hand = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
hand4 = updateHand(hand, 'hello')
print(hand)
print(hand4)


