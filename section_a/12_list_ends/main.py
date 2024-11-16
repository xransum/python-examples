"""List Ends.

Write a program that takes a list of
numbers, for example:

---
a = [5, 10, 15, 20, 25]
---

and makes a new list of only the first and
last elements of the given list. For
practice, write this code inside a
function.
"""

def str_to_nums(text):
    """Convert text with differing delimiters to list of numbers."""
    numbers = []
    if "," in stdin:
        numbers = [int(n.strip()) for n in stdin.split(",")]
    else:
        numbers = [int(n.strip()) for n in stdin.split(" ")]
    return numbers


def list_first_last(elems):
    """Get first and last list elements."""
    return elems[0], elems[-1]


stdin = input("Input list of numbers: ").strip()
numbers = str_to_nums(stdin)
first, last = list_first_last(numbers)

print(first, last)
