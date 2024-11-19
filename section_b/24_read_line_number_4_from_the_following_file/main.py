"""Read line number 4 from the following file."""

import os


def read_file(file_path):
    """Gets contents of file."""
    with open(file_path, "r") as file:
        return file.read()


root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root, "test.txt")
lines = read_file(file_path).split("\n")

for i in range(len(lines)):
    line = lines[i]
    if i == 3:
        print(line)