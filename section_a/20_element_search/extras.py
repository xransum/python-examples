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

def binary_search(
    num: int,
    items: list,
) -> bool:
    """Search for element using Binary search, slicing lists."""
    if len(items) > 1:
        # Use int() to round down when length is not divisble by 2
        middle_i = int((len(items) / 2))
        middle_n = items[middle_i]
        
        # Slice items into middle
        left = items[:middle_i]
        right = items[middle_i + 1:]
        
        # Middle number equals num
        if middle_n == num:
            return True
        # Loop back around
        elif num < middle_n:
            return binary_search(num, left)
        else:
            return binary_search(num, right)
        
    else:
        # Check element in list since
        return num in items


contains = binary_search(rng_num, rng_list)
print(f"List has {rng_num}: {contains}")