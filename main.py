# https://script.google.com/macros/s/AKfycbweiJqN8ffDiu3V508ASyN6hPy77y89h28FVGNos90JS7LYbW1gPC2B0PUKbN0rO3m0/exec


import requests
import json
import random

# Google Apps Script Web API URL (replace with your actual deployment URL)
API_URL = "https://script.google.com/macros/s/AKfycbweiJqN8ffDiu3V508ASyN6hPy77y89h28FVGNos90JS7LYbW1gPC2B0PUKbN0rO3m0/exec"

def submit_score(player, score, game_hash):
    data = {"player": player, "score": score, "hash": game_hash}
    response = requests.post(API_URL, json=data)
    print(response.text)

# Game Logic
def number_guess_game():
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 100)  # Generate a random number
    player_name = input("Enter your name: ")
    guess = int(input("Guess a number between 1 and 100: "))

    # Calculate score (closer = higher score)
    score = max(0, 100 - abs(secret_number - guess))

    # Simple hash (could be improved)
    game_hash = str(hash("fixed_game_hash"))

    print(f"The correct number was {secret_number}. Your score: {score}")

    # Submit score to Google Sheets
    submit_score(player_name, score, game_hash)

# Run the game
number_guess_game()