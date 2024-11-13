"""List Remove Duplicates.

Write a program (function!) that takes a
list and returns a new list that contains
all the elements of the first list minus
all the duplicates.

Extras:
    - Write two different functions to do
      this - one using a loop and
      constructing a list, and another
      using sets.
    - Go back and do Exercise 5 using
      sets, and write the solution for
      that in a different function.
"""

from random import randint

def generate_list(length):
    """Create a list of N length."""
    return [randint(0, 25) for i in list(range(length))]


def dedupe_a(items):
    """Remove duplicates from a given list."""
    new_list = []
    for i in items:
        if i not in new_list:
            new_list.append(i)
    return new_list


def dedupe_b(items):
    return list(set(items))


items = generate_list(25)
deduped_a = dedupe_a(items)
deduped_b = dedupe_b(items)

print(f"Full List: {items}")
print(f"Dedupe List A: {deduped_a}")
print(f"Dedupe List B: {deduped_b}")
