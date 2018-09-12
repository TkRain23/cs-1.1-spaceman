import random  # import library of functions -- random numbers


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
    return secret_word


def display_board(secret_word):
    for i in range(len(list(secret_word))-1):
        print("_", end=' ')

    print("_")



def start_game(secret_word):
    print("Your secret word contains {} characters.".format(len(secret_word)))
    print("Guess one letter per round -- good luck!")
    display_board(secret_word)


def spaceman(function_code):
    print("Welcome to Spaceman: Press 'A' to Begin")
    if function_code == "A" or function_code == "a":
        # load the game
        start_game(load_word())


spaceman("A")
