"""

Gr8 Hangman Game

Manuela C.

"""

"""
thu nov 16

strikes still dont work

but display hang is fixed

"""

strikes = 0
limit = 6


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

def display_board(solved, strikes):
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

        
    print(solved)


def show_result(strikes, limit):
    if strikes <= limit:
        print("You win!")

    if strikes > limit:
        print("You lose!")
        
    
def play(strikes, limit):
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)

    strikes = 0
    limit = 6

    display_board(solved, strikes)

    print("Guess a letter:")

    print("")
    print("")

    
    while solved != puzzle:
        letter = get_guess()
        
        if letter not in puzzle:
            strikes += 1


        if strikes > limit:
            show_result(strikes, limit)
        if puzzle == solved:
            show_result(strikes, limit)

        
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved, strikes)

    show_result(strikes, limit)

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.casefold()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")


def show_credits():
    print("")
    print("Manuela C.")
    print("November 21")
    print("")


show_splash_screen()
    
playing = True

while playing:
    play(strikes, limit)
    playing = play_again()

show_credits()

