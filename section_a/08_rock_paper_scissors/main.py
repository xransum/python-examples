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

    player_a = options[int(input("Player A - Select: ")) - 1]
    player_b = options[int(input("Player B - Select: ")) - 1]

    print(f"\nPlayer A: {player_a.capitalize()}, Player B: {player_b.capitalize()}")

    if player_a == player_b:
        print("Tie Game!")

    elif player_a == "rock" and player_b == "scissors":
        print("Player A Wins!")

    elif player_a == "paper" and player_b == "rock":
        print("Player A Wins!")

    elif player_a == "scissors" and player_b == "paper":
        print("Player A Wins!")

    else:
        print("Player B Wins!")

    print()

    confirm = input("Play again? (y/n) ").strip().lower()
    if len(confirm) <= 0 or confirm[0] == "n":
        break

    print()
