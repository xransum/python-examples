"""Check Primality Functions.

Ask the user for a number and determine
whether the number is prime or not. (For
those who have forgotten, a prime number
is a number that has no divisors.). You
can (and should!) use your answer to
Exercise 4 to help you. Take this
opportunity to practice using functions,
described below.
"""

num = int(input("Input Number: "))

divisables = []
for i in range(1, num + 1):
    # Check if remainder is whole number
    if (num / i) % 1 == 0:
        divisables.append(i)

if len(divisables) == 2:
    print(f"{num} is a Prime Number.")

else:
    print(f"{num} is NOT a Prime Number.")
