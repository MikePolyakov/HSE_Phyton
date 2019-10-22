def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score

    # As long as there are still letters left in the hand:

    # Display the hand

    # Ask user for input

    # If the input is a single period:

    # End the game (break out of the loop)

    # Otherwise (the input is not a single period):

    # If the word is not valid:

    # Reject invalid word (print a message followed by a blank line)

    # Otherwise (the word is valid):

    # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line

    # Update the hand

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score


filename = 'words.txt'
wordList = []
file = open(filename).read().split('\n')
for line in file:
    wordList.append(line.lower())
hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
word = "quail"

print(playHand(word, wordList, ))

'''
Test Cases to Understand the Code: 
>>> compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6) 
appels 
>>> compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5) 
acta 
>>> compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12) 
immanent 
>>> compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12) 
None
'''