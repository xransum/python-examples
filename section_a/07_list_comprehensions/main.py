"""List Comprehensions.

Let’s say I give you a list saved in a
variable:
---
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
---

Write one line of Python that takes this
list a and makes a new list that has only
the even elements of this list in it.
"""

list_a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list_b = [a for a in list_a if a % 2 == 0]

print(list_b)