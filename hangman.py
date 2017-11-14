"""

Gr8 Hangman Game

Manuela C.

"""
def show_splash_screen():

    print("_____________________  ")
    print("| .__________))______| ")
    print("| | / /      ||        ")
    print("| |/ /       ||        ")
    print("| | /        ||.-''.   ")
    print("| |/         |/  _  \  ")
    print("| |          ||  `/,|  ")
    print("| |          (\\  U .'   ")
    print("| |         .-`--'.    ")
    print("| |        /Y . . Y\   ")
    print("| |       // |   | \\\  ")
    print("| |      //  | . |  \\\ ")
    print("| |     ')   |   |   (`")
    print("| |          || ||     ")
    print("| |          || ||     ")
    print("| |          || ||     ")
    print("| |          || ||     ")
    print("| |         / | | \    ")
    print("''''''''''|_`-' `-' |''''|")
    print("|'|'''''''\ \       ''|'| ")
    print("| |        \ \        | | ")
    print(": :         \ \       : : ")
    print(". .          `'       . . ")
    print("  _      ______ _______ _  _____ ")
    print(" | |    |  ____|__   __( )/ ____|")
    print(" | |    | |__     | |  |/| (___  ")
    print(" | |    |  __|    | |     \___ \ ")
    print(" | |____| |____   | |     ____) |")
    print(" |______|______|  |_|    |_____/ ")
    print("")
    print("   _____ ______ _______") 
    print("  / ____|  ____|__   __|")
    print(" | |  __| |__     | |   ")
    print(" | | |_ |  __|    | |   ")
    print(" | |__| | |____   | |   ")
    print("  \_____|______|  |_|   ")
    print("")
    print("  _    _          _   _  _____ _____ _   _  _____ ")
    print(" | |  | |   /\   | \ | |/ ____|_   _| \ | |/ ____|")
    print(" | |__| |  /  \  |  \| | |  __  | | |  \| | |  __ ")
    print(" |  __  | / /\ \ | . ` | | |_ | | | | . ` | | |_ |")
    print(" | |  | |/ ____ \| |\  | |__| |_| |_| |\  | |__| |")
    print(" |_|  |_/_/    \_\_| \_|\_____|_____|_| \_|\_____|")
    print("")
    print("")
                                                  



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
    letter = input()
    return letter

def display_board(solved):
    print(solved)


def show_result():
    print("You Won!")
    
def play():
    show_splash_screen()
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)

    strikes = 0
    limit = 6

    print("")
    print("")

    print("     _________ ")
    print("    |         |")
    print("    |         ")
    print("    |        ")
    print("    |        ")
    print("    |")
    print("    |")

    print("")
    print("")

    print("Guess a letter:")

    print("")
    print("")

    print(solved)



    
    while solved != puzzle:
        letter = get_guess()
        
        if letter not in puzzle:
            strikes += 1

            if strikes == 1:
                print("     _________ ")
                print("    |         |")
                print("    |         0")
                print("    |        ")
                print("    |        ")
                print("    |")
                print("    |")

            if strikes == 2:
                print("     _________ ")
                print("    |         |")
                print("    |         0")
                print("    |         |")
                print("    |        ")
                print("    |")
                print("    |")

            if strikes == 3:
                print("     _________ ")
                print("    |         |")
                print("    |         0")
                print("    |         |\\ ")
                print("    |        ")
                print("    |")
                print("    |")

            if strikes == 4:
                print("     _________ ")
                print("    |         |")
                print("    |         0")
                print("    |        /|\\ ")
                print("    |        ")
                print("    |")
                print("    |")

            if strikes == 5:
                print("     _________ ")
                print("    |         |")
                print("    |         0")
                print("    |        /|\\ ")
                print("    |          \\ ")
                print("    |")
                print("    |")

            if strikes == 6:
                print("     _________ ")
                print("    |         |")
                print("    |         0")
                print("    |        /|\\ ")
                print("    |        / \\ ")
                print("    |")
                print("    |")




        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)

    show_result()

play()
