# Hangman game
#

# -----------------------------------
# Helper code
"""

The computer must select a word at random from the list of available words that was provided in words.txt. The functions for loading the word list and selecting a random word have already been provided for you in ps3_hangman.py.

The game is interactive

At the start of the game, the user know how many letters the computer's word contains.

Ask the user to supply one guess (i.e. letter) per round.

The user  receive feedback immediately after each guess about whether their guess appears in the computer's word.

After each round, the program display to the user the partially guessed word so far, as well as letters that the user has not yet guessed.

Some additional rules of the game:
A user is allowed 8 guesses

A user loses a guess only when s/he guesses incorrectly.

The game  end when the user constructs the full word or runs out of guesses. If the player runs out of guesses (s/he "loses").
"""
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    wordSize = 0
    for char in secretWord:
        if char in lettersGuessed:
            wordSize += 1
    return wordSize == len(secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    newWord = ''
    for char in secretWord:
        if char in lettersGuessed:
            newWord += char
        else:
            newWord += '_ '
    return newWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availLetters = string.ascii_lowercase
    for char in lettersGuessed:
        if char in availLetters:
            availLetters = availLetters.replace(char, '')
    return availLetters
    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', str(len(secretWord)), 'letters long.')
    print('-----------')
    
    numGuesses = 8
    lettersGuessed = ['',]
    while True:
        print('You have', str(numGuesses),' guesses left.')
        print('Available letters: ', getAvailableLetters(lettersGuessed))
        letter = input('Please guess a letter: ')
        letter = letter.lower()
        if letter in secretWord and letter not in lettersGuessed:
            lettersGuessed.append(letter)
            print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))
        elif letter in lettersGuessed:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(letter)
            print('Oops! That letter is not in my word: ', getGuessedWord(secretWord, lettersGuessed))
            numGuesses -= 1
        print('------------')
        
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            break
        if numGuesses < 1:
            print('Sorry, you ran out of guesses. The word was else.')
            break
        


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
