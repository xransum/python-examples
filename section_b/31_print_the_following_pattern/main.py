"""Print the following pattern.

Write a Python program to print the
reverse number pattern using a for loop.

```
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
```
"""

for x in range(5, 0, -1):
    for y in range(x, 0, -1):
        print(f"{y} ", end="")

    print()