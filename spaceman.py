import random  # import library of functions -- random numbers
import os
import sys

intro = '''
 _____ _____ _____ _____ _____ _____ _____ _____
|   __|  _  |  _  |     |   __|     |  _  |   | |
|__   |   __|     |   --|   __| | | |     | | | |
|_____|__|  |__|__|_____|_____|_|_|_|__|__|_|___|
         '''

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def load_word():
    """
    load_word: Reads a text file and stores each word into a list.
    The list of words are separated by a single space.
    It then returns a random word from the list that will be used for the game.
    """
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    # print(list(secret_word))
    if '\n' in secret_word:
        secret_word = secret_word.replace('\n', '')

    return secret_word


def display_board(secret_word):
    for i in range(len(list(secret_word))-1):
        print("_", end=' ')

    print("_")


def update_board(secret_word, guessed_characters):
    blank_tiles = ["_"] * len(list(secret_word))
    solution_tiles = list(secret_word)
    for i, x in enumerate(solution_tiles):
        if x in guessed_characters:
            blank_tiles[i] = x
    for letter in blank_tiles:
        print(letter, end=' ')
    print(' ')

    if "_" not in letter:
        return True
    else:
        return False


def start_guessing(secret_word):
    guessed_characters = []
    incorrect_guess = 1
    while incorrect_guess < 8:
        characters = input("Enter a character: ").lower()
        guessed_characters.append(characters)
        if characters in secret_word:
            if update_board(secret_word, guessed_characters):
                print("You Win")
                return

        else:
            print("Wrong, Try Again: {}/7".format(incorrect_guess))
            incorrect_guess += 1
            if incorrect_guess == 8:
                selection = user_input("Game Over: Press 'A' to try again, Press 'Q' to quit. \n")
                spaceman(selection)

    """
    if user input matches any part of the string (secret word)
    display that word. in the dispplay block.

    otherwise return error message + increment error count by 1
    if error count reaches 7, end game + give option to restart

    if user enters same character, prompt user to enter a different one

    only take in single characters, no strings, no digits.

    """


def start_game(secret_word):
    print("Your secret word contains {} characters.".format(len(secret_word)))
    print("Guess one letter per round -- good luck!")
    display_board(secret_word)
    start_guessing(secret_word)


def spaceman(function_code):
    if function_code.upper() == "A":
        # load the game
        os.system('clear')
        start_game(load_word())

    if function_code.upper() == "Q":
        sys.exit()


running = True
while running:
    print(intro)
    selection = user_input("Welcome to Spaceman: Press 'A' to Begin \n")
    running = spaceman(selection)
