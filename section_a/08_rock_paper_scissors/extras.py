"""Rock Paper Scissors.

Make a two-player Rock-Paper-Scissors
game. (Hint: Ask for player plays (using
input), compare them, print out a message
of congratulations to the winner, and ask
if the players want to start a new game).

Remember the rules:
   - Rock beats scissors
   - Scissors beats paper
   - Paper beats rock

Extras:
   - Create a bot that randomly selects an
     option.
"""
from random import randint

options = [
    "rock",
    "paper",
    "scissors",
]

while True:
    print("Options -")
    for i in range(len(options)):
        option = options[i]
        print(f"    {i+1}. {option.capitalize()}.")

    bot = options[randint(0, len(options) - 1)]
    user = options[int(input("Select: ")) - 1]

    print(f"\nUser: {user.capitalize()}, Bot: {bot.capitalize()}")

    if user == bot:
        print("Tie Game!")

    elif user == "rock" and bot == "scissors":
        print("User Wins!")

    elif user == "paper" and bot == "rock":
        print("User Wins!")

    elif user == "scissors" and bot == "paper":
        print("User Wins!")

    else:
        print("Bot Wins!")

    print()

    confirm = input("Play again? (y/n) ").strip().lower()
    if len(confirm) <= 0 or confirm[0] == "n":
        break

    print()
