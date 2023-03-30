import requests
from bs4 import BeautifulSoup

response = requests.get(
url="https://www.imdb.com/title/tt1745960/?ref_=nv_sr_srsg_0",
)
print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')

rating = soup.find(id="hero-rating-bar__aggregate-rating__score")
print(rating)