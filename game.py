import random

#Definitions aka Python functions because python gotta be all yew-neek
#Pycharm just made me spend way too long learning about something called PEP8 or basically readability conventions, so apparently
#I'm 'supposed' to name functions with snake_case instead of camelCase

def sanitized_guess():
    """
    This function is used to sanitize input for guesses and should be assigned to a variable.
    It will return an integer based on user input and will repeat until the user enters a valid integer.
    """
    # putting this in a whilever loop will make sure that the input is valid while also preventing the recursion. Beforehand we were calling the funciton inside itself
    while True:
        guess = input("Please guess a number.\n")

        #https://docs.python.org/3/tutorial/errors.html#handling-exceptions
        try:
            guess = int(guess)
            return guess
        except ValueError:
            print("Sorry, we only accept integers. Please try again.")
def yes_no(prompt):
    print(str(prompt))
    while True:
        try:
            a = input()
            a = a.lower()
            if a == "y" or "yes":
                return 1
            elif a == "n" or "no":
                return 0
        except ValueError:
            print("Invalid option. Please try again...\n")


def comparator(a, b):
    """
    Returns a string regarding the status of the guess after comparing 2 variables.
    :param a: A valid integer (The player's guess)
    :param b: A valid integer (The secret number)
    :return: Output
    """
    if a == b:
        return "You Won!"
    elif a < b:
        return "Your number is less than the secret number."
    elif a > b:
        return "Your number is greater than the secret number"
    else:
        return "Error"
# Game Loop 1: generate random number, 2: have player guess until they get it right, 3: let player restart game from step 1
# Get this done

secretNumber = random.randint(1, 100)

name = input("What is your name?\n")
gameOn = True
while gameOn:
    guess = sanitized_guess()
    print(comparator(guess, secretNumber))
    if comparator(guess, secretNumber) == "You Won!":
        gameOn = False
yes_no("Would you like to play again")