"""Write To A File.

Take the code from the "How To Decode A
Website" exercise (if you didn’t do it or
just want to play with some different
code, use the code from the solution), and
instead of printing the results to a
screen, write the results to a txt file.

In your code, just make up a name for the
file you are saving to.

Extras:
    - Ask the user to specify the name of
      the output file that will be saved.
"""
import os
import requests
from bs4 import BeautifulSoup


article_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"

def get_page(url):
    """Get a webpage as soup."""
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup


# Get the page as soup and target elements
soup = get_page(article_url)
elems = soup.find_all("div", class_="article__body")
text = "\n\n".join([e.get_text() for e in elems])

# Get current directory of this file
root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root, "file.txt")

print(f"Writing to file: {file_path}")

with open(file_path, "w", encoding="utf-8") as file:
    bytes = file.write(text)
    print(f"Successfully wrote {bytes} bytes!")


