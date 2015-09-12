from __future__ import print_function
import random

HANGMANPICS = ['''

 +---+
 |   |
     |
     |
     |
     |
=========''','''

 +---+
 |   |
 O   |
     |
     |
     |
=========''','''

 +---+
 |   |
 O   |
 |   |
     |
     |
=========''','''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''','''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''','''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''','''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret goat goose hawk lion lizard llama mole monkey moose mouse mule own panda parrot pigeon python rabbit ram rat raven  rhino salmon seal shark sheep skunk slot snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    #This function returns a random string from the passed list of string.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_'*len(secretWord)

    for i in range(len(secretWord)): #replace blanks with correct guesses
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: #show the secret word spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    #Returns the letter the player already entered.
    #This function makes sure the player enetered a single letter.
    while True:
        print('Guess a letter.')
        guess = raw_input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    #this function returns True if the player wants to play again, else False
    print('Do you want to play again? (yes or no)')
    return raw_input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # Let the plater type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters,
                secretWord)
            print('You have run out of guesses!\nAfter ' 
                + str(len(missedLetters)) + ' missed guesses and '
                + str(len(correctLetters)) + ' correct guesses, the word '
                + 'was "' + secretWord + '"')
            gameIsDone = True

    # Ask if they want to playa gain (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
