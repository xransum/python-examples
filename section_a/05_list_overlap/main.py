"""List Overlap.

Take two lists, say for example these two:

---
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
     12, 13]
---

and write a program that returns a list
that contains only the elements that are
common between the lists (without
duplicates). Make sure your program works
on two lists of different sizes.

Extras:
    - Randomly generate two lists to test
      this.
    - Write this in one line of Python
      (don’t worry if you can’t figure
      this out at this point - we’ll get
      to it soon).
"""

list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34,
          55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          11, 12, 13]

overlaps = []
for a in list_a:
    if a not in list_b and a not in overlaps:
        overlaps.append(a)

print(f"List A: {list_a}")
print(f"List B: {list_b}")
print(f"Overlaps: {overlaps}")


