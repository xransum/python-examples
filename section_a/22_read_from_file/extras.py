"""Read From File.

Given a .txt file that has a list of a
bunch of names, count how many of each
name there are in the file, and print out
the results to the screen. I have a .txt
file for you, if you want to use it!

Extra:
    - Instead of using the .txt file from
      above (or instead of, if you want
      the challenge), take this .txt file,
      and count how many of each
      "category" of each image there are.
      This text file is actually a list of
      files corresponding to the SUN
      database scene recognition database,
      and lists the file directory
      hierarchy for the images. Once you
      take a look at the first line or two
      of the file, it will be clear which
      part represents the scene category.
      To do this, you’re going to have to
      remember a bit about string parsing
      in Python 3. I talked a little bit
      about it in this post.

References:
    - Sample .txt File: https://www.practicepython.org/assets/nameslist.txt
    - Sample SUN DB File: https://www.practicepython.org/assets/Training_01.txt
    - SUN Database: https://groups.csail.mit.edu/vision/SUN/hierarchy.html
"""
import os

# Get current directory of this file
root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root, "training_data.txt")


def read_file(file_path):
    """Read a files contents."""
    with open(file_path, "r") as file:
        return file.read()


contents = read_file(file_path)
rows = [l.strip() for l in contents.split("\n") if l != ""]

# Split rows by "/" and trim first empty element
sections = [r.split("/")[1:] for r in rows]

categories_count = {}

for segs in sections:
    alpha = segs[0]
    image = segs[-1]
    # Sometimes the entry has a sub-category
    category = "_".join(segs[1:-1])

    if category not in categories_count:
        categories_count[category] = []

    categories_count[category].append(image)


categories_count_sorted = sorted(
    list(categories_count.items()),
    key=lambda c: len(c[-1]),
    reverse=True,
)

for category, images in categories_count_sorted:
    print(f"{category}: {len(images)}")
