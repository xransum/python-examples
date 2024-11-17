"""Find the number of occurrences of a substring in a string.

Write a Python code to find how often the
substring “Emma” appears in the given
string.

Given:

```bash
str_x = "Emma is good developer. Emma is a writer"
```

Expected Output:

```
Emma appeared 2 times
```
"""

str_x = "Emma is good developer. Emma is a writer"

count = 0
targ_word = "Emma"

for word in str_x.split(" "):
    if targ_word in word:
        count += 1


print(f"{targ_word} appeared {count} times")
