"""Merge two lists using the following condition.

Given two lists of numbers, write a Python
code to create a new list such that the
latest list should contain odd numbers
from the first list and even numbers from
the second list.

Given:

```python
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
```

Expected Output:

```
result list: [25, 35, 40, 60, 90]
```
"""

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

list3 = []
list3.extend([n for n in list1 if n % 2 != 0])
list3.extend([n for n in list2 if n % 2 == 0])

print(f"result list: {list3}")