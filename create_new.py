"""Script to easily create new example directories.
"""
import sys
import os
import re
from glob import glob

DIR_REGEX = r"^[0-9]+_"
SECTIONS_REGEX = r"section_[a-z]"

root = os.path.dirname(os.path.abspath(__file__))

sections_names = sorted([d for d in os.listdir(root) if re.search(SECTIONS_REGEX, d) is not None])

print("Section select -")
for i in range(len(sections_names)):
    section_name = sections_names[i]
    print(f"{i + 1}. {section_name}")

section_name = sections_names[
    int(input("Selection: ").strip()) - 1
]
section_dir = os.path.join(
    root,
    section_name,
)
dirs = [
    d for d in os.listdir(section_dir) if (
        os.path.isdir(d) and re.search(DIR_REGEX, d) is not None)
]
sample_title = input("Title Name: ").strip()
new_dir_name = "_".join(
    re.findall(r"\w+", sample_title.strip().lower()),
)
new_dir_path = os.path.join(
    section_dir,
    f"{str(len(dirs) + 1).rjust(2, '0')}_{new_dir_name}",
)

for dir_name in dirs:
    name = re.sub(DIR_REGEX, "", dir_name)
    if name == new_dir_name:
        print(f"Dir name exists: {new_dir_name} under {dir_name}.")
        sys.exit(1)

print(new_dir_path)

baseline_header = f'''"""{sample_title}.

"""

'''

try:
    os.mkdir(new_dir_path)
    with open(os.path.join(new_dir_path, "main.py"), "w", encoding="utf-8") as f:
        f.write(baseline_header)
except:
    print("Failed to create new example!")
    sys.exit(1)

# Clean exit
sys.exit(0)