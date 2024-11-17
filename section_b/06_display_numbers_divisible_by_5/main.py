"""Display numbers divisible by 5.

Write a Python code to display numbers
from a list divisible by 5

Expected Output:

```
Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55
```
"""

def divisble_by(numbers, div):
    """Get numbers divisible by n."""
    list_n = []
    for n in numbers:
        if n % div == 0:
            list_n.append(n)

    return list_n


numbers_a = [10, 20, 33, 46, 55]
print(f"Given {numbers_a}")

print("Divisible by 5")
div_five = divisble_by(numbers_a, 5)
for n in div_five:
    print(n)
