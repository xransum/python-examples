"""Check file is empty or not.

Write a program to check if the given file
is empty or not
"""

import os


def get_file_size(file_path):
    """Gets the file size in bytes."""
    file_stats = os.stat(file_path)
    return file_stats.st_size


root = os.path.dirname(os.path.abspath(__file__))

for i in range(1, 3):
    file_name = f"file_{i}.txt"
    file_path = os.path.join(root, file_name)
    if get_file_size(file_path) == 0:
        print(f"File {file_name} is empty.")
    else:
        print(f"File {file_name} is not empty.")