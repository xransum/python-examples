"""Accept a list of 5 float numbers as an input from the user.

Expected Output:

```python
[78.6, 78.6, 85.3, 1.2, 3.5]
```
"""

nums = []

for i in range(0, 5):
    x = float(input(f"Enter Number {i + 1}: "))
    nums.append(x)

print(nums)