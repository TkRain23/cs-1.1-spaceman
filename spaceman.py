import random  # import library of functions -- random numbers
import collections


def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    print(list(secret_word))
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.
    This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean,
    True only if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    # checks to see if the length matches first
    if length.secret_word == length.letters_guessed:
        # turns secret_word into a list of characters
        # compares it to the list of letters guessed
        if set(list(secret_word)) == set(letters_guessed):
            return true
    else:
        return false


def get_guessed_word(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.
    This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.
    For letters in the word that the user has guessed correctly,
    the string should contain the letter at the correct position.
    For letters in the word that the user has not yet guessed,
    shown an _ (underscore) instead.
    '''


def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    theAlphabet = []
    for letter in range(97, 123):
        theAlphabet.append(chr(letter))
    myAlphabet = theAlphabet[:]


load_word()
