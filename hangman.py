"""

Gr8 Hangman Game

Manuela C.

"""
def show_splash_screen():

    print("___________.._______
    print("| .__________))______|
    print("| | / /      ||
    print("| |/ /       ||
    print("| | /        ||.-''.
    print("| |/         |/  _  \
    print("| |          ||  `/,|
    print("| |          (\\`_.'
    print("| |         .-`--'.
    print("| |        /Y . . Y\
    print("| |       // |   | \\
    print("| |      //  | . |  \\
    print("| |     ')   |   |   (`
    print("| |          ||'||
    print("| |          || ||
    print("| |          || ||
    print("| |          || ||
    print("| |         / | | \
    print("""""""""""|_`-' `-' |"""|
    print("|"|"""""""\ \       '"|"|
    print("| |        \ \        | |
    print(": :         \ \       : :
    print(". .          `'       . .


def get_puzzle():
    return "hangman"

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    letter = input("Guess a letter:")
    return letter

def display_board(solved):
    print(solved)

def show_result():
    print("You Won!")
    
def play():
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)

    strikes = 0
    limit = 6

    print(solved)
    
    while solved != puzzle:
        letter = get_guess()
        
        if letter not in puzzle:
                pass
            
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)

    show_result()

play()
