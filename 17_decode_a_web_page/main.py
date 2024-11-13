"""Decode A Web Page.

Use the BeautifulSoup and requests Python
packages to print out a list of all the
article titles on the New York Times
homepage.

Target Page: https://www.nytimes.com/

THIS IS WORK IN PROGRESS!
"""

import requests
from bs4 import BeautifulSoup
import re
import json


nyt_homepage = "https://www.nytimes.com/"

def get_page(url):
    """Get a webpage as soup."""
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    if res.status_code != 200:
        print("Non-200 Response Code Recieved!")
    return soup


soup = get_page(nyt_homepage)
scripts = soup.find_all("script")
script = next(e for e in scripts if "window.__preloadedData" in e.get_text()).get_text()
raw_json = re.sub(r"\bundefined\b", "null", re.sub(r"^window.__preloadedData = |\;$", "", script))

data = json.loads(raw_json)
with open("fug.txt", "w") as f:
    json.dump(data, f, indent=4)