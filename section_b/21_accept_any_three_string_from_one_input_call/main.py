"""Accept any three string from one input() call.

Write a program to take three names as
input from a user in the single input()
function call.

Expected Output:

```
Enter three string Emma Jessa Kelly
Name1: Emma
Name2: Jessa
Name3: Kelly
```
"""

value = input("Enter three string: ")
names = value.split(" ")

for i in range(len(names)):
    name = names[i]
    print(f"Name{i + 1}: {name}")