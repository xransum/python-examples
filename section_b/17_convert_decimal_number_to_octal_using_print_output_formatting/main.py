"""Convert Decimal number to octal using print() output formatting.

Given:

```python
num = 8
```

Expected Output:

The octal number of decimal number 8 is 10
"""

x = int(input("Number: "))
octal = "%o" % x

print(f"The octal number of decimal number {x} is {octal}")