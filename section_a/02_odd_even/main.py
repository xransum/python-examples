"""Odd Or Even.

The exercise comes first (with a few
extras if you want the extra challenge or
want to spend more time).

Ask the user for a number. Depending on
whether the number is even or odd, print
out an appropriate message to the user.
Hint: how does an even / odd number react
differently when divided by 2?

Extras:
    - If the number is a multiple of 4,
      print out a different message.
    - Ask the user for two numbers: one
      number to check (call it num) and
      one number to divide by (check). If
      check divides evenly into num, tell
      that to the user. If not, print a
      different appropriate message.
"""

num_a = int(input("1st Number: ").strip())
num_b = int(input("2nd Number: ").strip())

num_div = num_a / num_b

if num_a % 2 == 0:
    print("Even Number.")

else:
    print("Odd Number.")
