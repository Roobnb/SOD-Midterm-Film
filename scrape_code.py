import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Top_Gun:Maverick"

print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')

rating = soup.find_all("Pass")
print(rating)
