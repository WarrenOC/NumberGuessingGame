# Ultimate Python Number Guessing Game
This number guessing game is a project I made for my CS220 computer science class. We were tasked with writing a number guessing game and I wanted to add my own little twists to make it more interesting since I had already done this project many times before for other classes.

The base assignment requirements were as follows:

* Your program MUST have a comment at the top containing your name, the date, and a description of the game.
* The game must start by asking for the player's name. It can then use that name in creative ways, such as "Lucky guess, Ralph!" or "Thanks for playing, Samantha!"
* Next, the program chooses a random number between 1 and 100.
* The player repeatedly guesses the number, and the program provides feedback such as "too high" or "too low."
* The program should count how many guesses the player makes and report that at the end.
* Once the player guesses the correct number, the program should announce that the game is over, and it should end.

Now I have taken some creative liberties and added a few features of my own as well as excluding the total number of guesses at the end. It was something that I considered irrelevant and decided to omit given the way the game is designed.

# New Features
## Game Modes and Difficulties
There are now 2 distinct gamemodes for players to choose from. Each gamemode has 3 seperate difficulties for you to choose from.
* Unlimited - The player will have as many guesses as they need and the game will be completed when the correct number is guessed. Choosing difficulties will change the range in which you will be guessing from. Your score will be how many guesses it took you to get the right number. In this game less is better.
* Limited Guesses - Players will only have so many guesses the amount of which is dependent on the difficulty they select. In this gamemode your score is based on how close your guesses were to the number. If you guess the correct number remaining guesses will be included in your score for the maximum possible value. Technically the score is a cumulative measure of accuracy so the higher the better. 

## Online ranking
I've connected my game to a google sheets GScript so that when a game is completed the score is uploaded and appended to a sheet for that gamemode and difficulty. Once the score has been successfully uploaded it will pull the top 5 scores from the leaderboard and display them along with the usernames of each of those players.

## Anti-Cheat
Since this game is connected to a scoreboard and the source code is publicly available I had to find a way to at least obscure players from just editing the submit score function to give them an impossibly high score. I've done this by making the leaderboard authenticate any score submission by requiring the hash of the main.py file making it so that changing the source code will change the hash and prevent the score from being added to the leaderboard. While this isn't tamper-proof it is a big step in securing the leaderboards.