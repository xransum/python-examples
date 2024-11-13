"""Element Search.

Write a function that takes an ordered
list of numbers (a list where the elements
are in order from smallest to largest) and
another number. The function decides
whether or not the given number is inside
the list and returns (then prints) an
appropriate boolean.

Extras:
    - Use binary search.
"""
from random import randint

# Generate a list of 50 elements containing a random number
# between 0-5000.
max_num = 50
rng_list = list(sorted(set([randint(0, max_num) for _ in range(50)])))
rng_num = randint(0, max_num)

print(f"List: {rng_list}")
print(f"Number: {rng_num}")

def search(
    num: int,
    items: list,
) -> bool:
    """Search for element is in list."""
    for i in items:
        if i == num:
            return True

    return False
    # Alt: return num in items

contains = search(rng_num, rng_list)
print(f"List has {rng_num}: {contains}")
