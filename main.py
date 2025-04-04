import random
import hashlib
import requests

# Google Apps Script Web App URL (Replace with your actual URL)
GOOGLE_SHEETS_URL = "https://script.google.com/macros/s/AKfycbz0sMrDJWyDkWfxXr15PE_CU2PzbLLBJjj98SWiHnxQF_uqXPS9tn9PI3Q5KaVhGKuu/exec"


def generate_code_hash():
    """Reads the current Python file and generates a SHA-256 hash."""
    try:
        with open(__file__, "rb") as f:  # Open this script file
            file_contents = f.read()
        return hashlib.sha256(file_contents).hexdigest()
    except:
        return "ERROR: Could not generate hash."  # If running in an environment without __file__ (like Google Colab)

def submit_score(name, score, mode, diff):
    # Generate hash of the script
    game_hash = generate_code_hash()

    # Send data to Google Sheets
    data = {
        "player": name,
        "score": score,
        "mode": mode,
        "difficulty": diff,
        "hash": game_hash
    }


    response = requests.post(GOOGLE_SHEETS_URL, json=data)
    print(response.text)  # Show server response

def numbered_input(prompt, n=2):
    yes_def = {"y": 1, "ye": 1, "yes": 1, "yep": 1, "sure": 1, "absolutely": 1}
    no_def = {"n": 2, "no": 2, "nope": 2,"nah": 2, "absolutely not": 2, "no way in hell": 2}

    while True:

        response = input(prompt).lower().strip()
        if response in yes_def:
            return yes_def[response]
        elif response in no_def:
            return no_def[response]
        try:
            choice = int(response)
            if 1 <= choice <= n:
                return choice
            else:
                print("Please pick an option between 1 and ", n)
        except ValueError:
            print("Please input a valid integer.")

def get_name():
    while True:
        name = input("What is your name?\n>")
        print("You have entered, \"",name,"\"")
        verify = numbered_input("Is this correct?\n[1] yes\n[2] no\n>")
        if verify == 1:
            return name



# The actual game loop.


name = get_name()

# f"string" voodoo type shit
too_high = [f"That was too high, {name}.", f"Your number was higher than the secret number, {name}.", f"Sorry, {name}, your number was too high."]
too_low = [f"That was too low, {name}.", f"Your number was lower than the secret number, {name}.", f"Sorry, {name}, your number was too low."]

while True:
    print("Welcome to the Ultimate Number Guessing Game (Now with online ranking and Anti-Cheat)\n")
    mode = numbered_input("What mode would you like?\n [1] Unlimited guesses\n [2] Limited Guesses\n>")



#Unlimited Guesses Mode
    if mode == 1:
        print("You have chosen Unlimited Guesses!")
        diff = numbered_input("What difficulty would you like to play?\n[1] Easy (1-100)\n[2] Medium (1-1000)\n[3] Hard (1-10000)\n>", 3)
        if diff == 1:
            max_number = 100
        elif diff == 2:
            max_number = 1000
        elif diff == 3:
            max_number = 10000

        secret_number = random.randint(1, max_number)
        guesses = 0

        # Actually start the guessing
        while True:
            # Insure the guesses are integers
            try:
                guess = int(input("Your guess: ").strip())
                if guess < 1 or guess > max_number:
                    print(f"Please input an integer between 1 and {max_number}")
                    continue
            except ValueError:
                print(f"Invalid input! Enter an integer between 1 and {max_number}.")

            #Increase the number of guesses to be calculated for score later
            guesses += 1

            if guess == secret_number:
                print("Congratulations, "+name+"! You correctly guessed the secret number!")
                break
            elif guess < secret_number:
                print(random.choice(too_low))
            elif guess > secret_number:
                print(random.choice(too_high))

        score = guesses


# Limited Guesses Mode
    elif mode == 2:
        print("You have chosen Limited Guesses")
        diff = numbered_input("What difficulty would you like to play?\n[1] Easy (15 Guesses)\n[2] Medium (10 Guesses)\n[3] Hard (5 Guesses)\n>", 3)
        max_number = 100
        distances = []

        if diff == 1:
            maxGuesses = 15
        elif diff == 2:
            maxGuesses = 10
        elif diff == 3:
            maxGuesses = 5
        else:
            print("If you're seeing this you are god.")
            maxGuesses = ["G", "O", "D"]

        secret_number = random.randint(1, max_number)
        guesses = 0

        while True:
            # Insure the guesses are integers
            try:
                guess = int(input("Your guess: "))
                if guess < 1 or guess > max_number:
                    print(f"Please input an integer between 1 and {max_number}")
                    continue
                else:
                    dist_score = max_number - abs(secret_number - guess)
                    distances.append(dist_score)

            except ValueError:
                print(f"Invalid input! Enter an integer between {1} and {max_number}.")
            #Increase the number of guesses to be calculated for score later
            guesses += 1
            if guess == secret_number:
                print("Congratulations, "+name+"! You correctly guessed the secret number!")
                break
            elif guess < secret_number:
                print(random.choice(too_low))
            elif guess > secret_number:
                print(random.choice(too_high))
            if guesses == maxGuesses:
                print(f"You ran out of guesses {name}")
                break

        score = sum(distances) / len(distances)

    print("Your score was: " + str(score))



    play_again = numbered_input("Would you like to play again?\n[1] yes\n[2] no\n>")
    if play_again == 1:
        continue
    elif play_again == 2:
        print ("Goodbye", name)
        break