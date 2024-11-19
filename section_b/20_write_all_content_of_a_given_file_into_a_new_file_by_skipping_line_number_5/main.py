"""Write all content of a given file into a new file by skipping line number 5.

Create a test.txt file and add the below
content to it.

Given test.txt file:

```
line1
line2
line3
line4
line5
line6
line7
```

Expected Output: new_file.txt

```
line1
line2
line3
line4
line6
line7
```
"""
import os


def read_file(file_path):
    """Read file contents."""
    with open(file_path, "r") as file:
        return file.read()


root = os.path.dirname(os.path.abspath(__file__))
contents = read_file(os.path.join(root, "test.txt"))
lines = contents.split("\n")
new_lines = [lines[i] for i in range(len(lines)) if i != 4]

with open(os.path.join(root, "new_file.txt"), "w") as file:
    file.write("\n".join(new_lines))