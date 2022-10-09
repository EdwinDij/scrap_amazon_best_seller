from urllib import request
import requests
from bs4 import BeautifulSoup
import soupsieve
url = "https://www.amazon.fr/gp/bestsellers/computers"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

tech_product_rank = []
tech_product_link = []
tech_product_name = []

rank = soup.find_all('span', class_='zg-bdg-text')

print(rank)