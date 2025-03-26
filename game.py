import random

#Definitions aka Python functions because python gotta be all yew-neek
#Pycharm just made me spend way too long learning about something called PEP8 or basically readability conventions so apparently
#I'm 'supposed' to name functions with snake_case instead of camelCase
def player_guess():
    # putting this in a whilever loop will make sure that the input is valid while also preventing the recursion. Beforehand we were calling the funciton inside itself
    while True:
        guess = input("Please guess a number.\n")

        #https://docs.python.org/3/tutorial/errors.html#handling-exceptions
        try:
            int(guess)
            return guess
        except ValueError:
            print("Sorry, we only accept integers. Please try again.")


# Game Loop 1: generate random number, 2: have player guess until they get it right, 3: let player restart game from step 1
# Todo
secretNumber = random.randint(1, 100)
name = input("What is your name?\n")
if guess == secretNumber:
    print("You won!")
else:
    print("You lost.")
