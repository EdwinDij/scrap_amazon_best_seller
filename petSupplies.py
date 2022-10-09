from unicodedata import name
import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.fr/gp/bestsellers/pet-supplies"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

supplies_product_name = []
supplies_product_rank = []
supplies_product_stars = []
rank = soup.find_all('span', class_='zg-bdg-text')
stars = soup.find_all('span', class_='a-icon-alt')
names = soup.find_all('div', class_='_cDEzb_p13n-sc-css-line-clamp-3_g3dy1')

def get_name ():
    for product_name in names:
        supplies_product_name.append(product_name.string)
    return supplies_product_name
get_name()

def get_rank ():
    for product_rank in rank:
        supplies_product_rank.append(product_rank.string)
    return supplies_product_rank
get_rank()

def get_stars():
    for product_stars in stars:
        supplies_product_stars.append(product_stars.string)
    return supplies_product_stars
get_stars()
