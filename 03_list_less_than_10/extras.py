"""List Less Than Ten.

Take a list, say for example this one:

---
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
---

and write a program that prints out all the elements of the list that are less than 5.

Extras:
    - Instead of printing the elements one
      by one, make a new list that has all
      the elements less than 5 from this
      list in it and print out this new
      list.
    - Write this in one line of Python.
    - Ask the user for a number and return
      a list that contains only elements
      from the original list a that are
      smaller than that number given by
      the user.
"""

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Extras 1
less_than_five_a = []
for num in numbers:
    if num < 5:
        less_than_five_a.append(num)


# Extras 2
less_than_five_b = [num for num in numbers if num < 5]

num_comp = int(input("Input Number: "))
less_than_n = [num for num in numbers if num < num_comp]

print(f"Numbers Less than 5, A: {less_than_five_a}.")
print(f"Numbers Less than 5, B: {less_than_five_b}.")
print(f"Numbers Less than {num_comp}: {less_than_n}.")
