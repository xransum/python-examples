"""Check if the first and last numbers of a list are the same.

Write a code to return True if the list’s
first and last numbers are the same. If
the numbers are different, return False.

Given:

```python
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
```

Expected Output:

```python
Given list: [10, 20, 30, 40, 10]
result is True

numbers_y = [75, 65, 35, 75, 30]
result is False
```
"""

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def first_last_match(list_a):
    """Check if the first and last numbers of a list are the same."""
    a_x, a_y = list_a[0], list_a[-1]

    return a_x == a_y


print(f"Given {numbers_x}")
print(f"result is {first_last_match(numbers_x)}")

print(f"Given {numbers_y}")
print(f"result is {first_last_match(numbers_y)}")

