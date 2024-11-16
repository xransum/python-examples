"""Print characters present at an even index number.

Write a Python code to accept a string
from the user and display characters
present at an even index number.

For example, str = "PYnative". so your
code should display ‘P’, ‘n’, ‘t’, ‘v’.

Expected Output:
```
Orginal String is  PYnative
Printing only even index chars
P
n
t
v
```
"""

value = input("Input a String: ")

print("Orginal String is %s" % value)
print("Printing only even index chars")

for i in range(len(value)):
    c = value[i]
    if i % 2 == 0:
        print(c)

