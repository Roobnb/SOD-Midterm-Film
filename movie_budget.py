import requests
from bs4 import BeautifulSoup
import re
import csv


def get_movie_budgets(url):
    budgets = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", class_="infobox vevent")
    rows = table.find_all("tr")
    for row in rows:
        if row.find("th") and "Budget" in row.th.text:
            budget_string = row.td.text.strip()
            # Extract numeric characters from budget string
            budget = re.findall(r"\d+\.*\d*", budget_string)[0]
            budgets.append(budget)
            break
    return budgets[0]
