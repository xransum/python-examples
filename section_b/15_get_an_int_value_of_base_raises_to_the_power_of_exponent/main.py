"""Get an int value of base raises to the power of exponent.

Write a function called exponent(base,
exp) that returns an int value of base
raises to the power of exp.

Note here exp is a non-negative integer,
and the base is an integer.

Expected output

Case 1:

```
base = 2
exponent = 5

2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)
```

Case 2:

```
base = 5
exponent = 4

5 raises to the power of 4 is: 625 
i.e. (5 *5 * 5 *5 = 625)
```
"""

def exponent(base, exp):
    """Get an int value of base raises to the power of exponent."""
    return base ** exp


print(exponent(2, 5))
print(exponent(5, 4))
