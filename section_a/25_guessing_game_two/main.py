"""Guessing Game Two.

In a previous exercise, we’ve written a
program that “knows” a number and asks a
user to guess it.

This time, we’re going to do exactly the
opposite. You, the user, will have in your
head a number between 0 and 100. The
program will guess a number, and you, the
user, will say whether it is too high, too
low, or your number.

At the end of this exchange, your program
should print out how many guesses it took
to get your number.

As the writer of this program, you will
have to choose how your program will
strategically guess. A naive strategy can
be to simply start the guessing at 1, and
keep going (2, 3, 4, etc.) until you hit
the number. But that’s not an optimal
guessing strategy. An alternate strategy
might be to guess 50 (right in the middle
of the range), and then increase /
decrease by 1 as needed. After you’ve
written the program, try to find the
optimal strategy!
"""
from random import randint

options = [
    "yes",
    "high",
    "low",
]


def guessing_game_two(
    min_num,
    max_num,
):
    """Guessing game part two."""
    lows = []
    highs = []

    input(f"Think of a number between {min_num} and {max_num}, hit ENTER when ready...")

    while True:
        guess = None
        if len(lows) + len(highs) == 0:
            guess = randint(min_num, max_num)
        else:
            # Set our new ranges for our guess
            highest_low, lowest_high = min_num, max_num
            if highest_low > lowest_high:
                print("Something went wrong, your high low of {highest_low} was greater than your lowest high numbers of {lowest_high}.")
                exit()
        
            if len(lows) > 0:
                highest_low = sorted(lows)[-1]

            if len(highs) > 0:
                lowest_high = sorted(highs)[0]

            guess = randint(highest_low + 1, lowest_high - 1)

        user = None
        while True:
            print(f"Is {guess} your number?")
            user = input("Low, High, or Yes: ").strip().lower()
            if user not in options:
                print("Invalid value, try again...")
            else:
                break

        if user == "high":
            highs.append(guess)
        elif user == "low":
            lows.append(guess)
        else:
            break

    print(f"It took {len(lows) + len(highs) + 1} guess(es) to get your number!")


def main():
    """Main function."""
    guessing_game_two(0, 100)


if __name__ == "__main__":
    main()