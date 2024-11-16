"""Guessing Game One.

Generate a random number between 1 and 9
(including 1 and 9). Ask the user to guess
the number, then tell them whether they
guessed too low, too high, or exactly
right. (Hint: remember to use the user
input lessons from the very first
exercise).

Extras:
    - Keep the game going until the user
      types "exit".
    - Keep track of how many guesses the
      user has taken, and when the game
      ends, print this out.
"""

from random import randint

min_num, max_num = 1, 9

# Game state variable
exit_game = False
while exit_game is False:
    print("> Guessing Game")
    # Generate a number and init user guesses
    rng_num = randint(min_num, max_num)
    guesses = []

    # Start current attempt
    while True:
        guess = input("Guess: ").strip()

        # Verify if value is a number
        if guess.isnumeric() is True:
            guess = int(guess)
            guesses.append(guess)

            # Compare the value and prompt user
            if guess == rng_num:
                print(f"Exactly right!")
                print(f"You got that in {len(guesses)} attempts.")
                break
            elif guess > rng_num:
                print(f"Too high!")
            else:
                print(f"Too low!")

        # Handle user exit
        elif guess == "exit":
            exit_game = True
            break

        # Catch overflow
        else:
            print("Invalid option, try again.")