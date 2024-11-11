"""Script to easily create new example directories.
"""
import sys
import os
import re
from glob import glob

root = os.path.dirname(os.path.abspath(__file__))
dirs = [d for d in os.listdir(root) if os.path.isdir(d)]
arg = input("Input: ").strip()
new_dir_name = "_".join(re.findall(r"\w+", arg.strip().lower()))
new_dir_path = os.path.join(root, f"{str(len(dirs) + 1).rjust(2, '0')}_{new_dir_name}")


for dir_name in dirs:
    name = re.sub(r"^[0-9]+_", "", dir_name)
    if name == new_dir_name:
        print(f"Dir name exists: {new_dir_name} under {dir_name}.")
        sys.exit(1)

print(new_dir_path)

baseline_header = f'''"""{arg}.

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