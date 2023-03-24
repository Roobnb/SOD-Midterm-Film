import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the Rotten Tomatoes page for a specific movie
urls = [
    "https://www.rottentomatoes.com/m/john_wick_chapter_4/reviews?intcmp=rt-scorecard_tomatometer-reviews"
]


all_review_data = []
# Send a GET request to the URL and parse the HTML using BeautifulSoup


for url in urls:

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

# Find the reviews section of the page and extract the review data
reviews_section = soup.find("div", {"id": "reviews"})
reviews = reviews_section.find_all("div", {"class": "review"})

# Create a list of dictionaries to store the review data
reviews_data = []
for review in reviews:
    critic = review.find("a", {"class": "unstyled bold articleLink"}).text.strip()
    publication = review.find("em").text.strip()
    rating = review.find("div", {"class": "review_icon"}).attrs["class"][1]
    review_text = review.find("div", {"class": "the_review"}).text.strip()
    reviews_data.append(
        {
            "critic": critic,
            "publication": publication,
            "rating": rating,
            "review_text": review_text,
        }
    )

all_review_data.extend(reviews_data)


reviews_df = pd.DataFrame(reviews_data)
