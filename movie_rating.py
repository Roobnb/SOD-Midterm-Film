import requests
from bs4 import BeautifulSoup
import re
import csv

#movies = ["12 Years a Slave", "American Hustle", "Captain Phillips (film)", "Dallas Buyers Club", "The Wolf of Wall Street (2013 film)"]


#define a function that tells the rating of a movie
def get_movie_rating(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")


    # Find all paragraphs in the page
    paragraphs = soup.find_all("p")


    # Loop through each paragraph and check if it contains the desired string
    for p in paragraphs:
        if ("average rating of " in p.get_text() or "average score of" in p.get_text()):
            text = p.get_text()
            # split all the text
            words = text.split()
            # Find the rating part of the text
            rating_index = words.index("average") + 3
            # Get the rating
            rating = words[rating_index]
            return rating
