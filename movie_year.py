import requests
from bs4 import BeautifulSoup
import re
import csv


def get_movie_year(url):
    # for movie in movies:
    #     url = f"https://en.wikipedia.org/wiki/{movie.replace(' ', '_')}"
    response = requests.get(url)
    movie_title = url.split("/")[-1].replace("_", " ").title()

    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    paragraphs = soup.find_all("p")
    for p in paragraphs:
        match = re.search(r"\b(20)\d{2}\b", p.get_text())
        if match:
            year = match.group(0)
            year = int(year)
            break
    return year
