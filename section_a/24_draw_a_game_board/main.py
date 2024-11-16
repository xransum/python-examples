"""Draw A Game Board.

This exercise is Part 1 of 4 of the Tic
Tac Toe exercise series. The other
exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we
want to draw game boards that look like
this:

```txt
 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
```

This one is 3x3 (like in tic tac toe).
Obviously, they come in many other sizes
(8x8 for chess, 19x19 for Go, and many
more).

Ask the user what size game board they
want to draw, and draw it for them to the
screen using Python’s print statement.

Remember that in Python 3, printing to the
screen is accomplished by:

```python
print("Thing to show on screen")
```
"""

def print_table(table):
    """Print a 2d array representing a game board."""
    height = len(table)

    for y in range(height):
        row = board[y]
        width = len(row)

        print(" ---" * width)

        for x in range(width):
            column = row[x]

            if x > 0:
                print(" ", end="")

            print("|", end="")
            print(f" {column}", end="")

            if x == width - 1:
                print(" |", end="")

        print()

    print(" ---" * width)


print("Input a Board Dimension, in the format of WxH (e.g. 3x3, 8x8, 19x19, etc.)")

width, height = [int(n) for n in input("Dimension: ").strip().split("x")]
# width, height = 5, 3

# Generate 2d Array representing the board
board = [[" "]*width]*height
print_table(board)

