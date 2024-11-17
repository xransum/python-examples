"""Script to build a listing of examples.
"""
import sys
import os
import re
from glob import glob


def read_file(file_path):
    """Read a files contents."""
    with open(file_path, "r") as file:
        return file.read()


def capitalize_words(value):
    """Capitalize words."""
    words = value.split(" ")
    return " ".join([w.capitalize() for w in words])


DIR_REGEX = r"^[0-9]+_.*$"
SECTIONS_REGEX = r"section_[a-z]"
HEADER_REGEX = r'"""(.|[\n\r])+?"""'

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sections_names = sorted([d for d in os.listdir(root) if re.search(SECTIONS_REGEX, d) is not None])

sections_with_subs = {section: {} for section in sections_names}

for section in sections_with_subs.keys():
    section_path = os.path.join(root, section)

    sub_sections = [d for d in os.listdir(section_path) if os.path.isdir(os.path.join(root, section, d)) is True]
    sorted_subsections = sorted(sub_sections,
        key=lambda k: int(k.split("_")[0]),
    )
    for sub_section in sorted_subsections:
        sub_path = os.path.join(root, section, sub_section)
        
        index = sub_section.split("_")[0]
        main_file = os.path.join(sub_path, "main.py")
        main_contents = read_file(main_file)
        heading = re.search(HEADER_REGEX, main_contents)[0].split("\"\"\"")[1]
        title = heading.split("\n")[0].strip()[0:-1]
        description = "\n".join(heading.split("\n")[1:]).strip()
        sections_with_subs[section][sub_section] = {
            "index": index,
            "title": title,
            "description": description,
        }


for section in sections_with_subs.keys():
    sub_sections = sections_with_subs[section]

    section_title = capitalize_words(" ".join(section.split("_")))
    print(f"- {section_title}")
    if len(sub_sections) == 0:
        print("   - None")
    else:

        for sub_section in sub_sections:
            sub_details = sub_sections[sub_section]
            print(f"   {int(sub_details.get('index'))}. [{sub_details.get('title')}](/{section}/{sub_section}/main.py)")