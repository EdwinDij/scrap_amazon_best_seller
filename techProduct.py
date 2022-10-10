import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.fr/gp/bestsellers/computers"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

tech_product_rank = []
tech_product_name = []
tech_product_stars = []
tech_product_price = []
rank = soup.find_all('span', class_='zg-bdg-text')
name = soup.find_all('div', class_='_cDEzb_p13n-sc-css-line-clamp-3_g3dy1')
stars = soup.find_all('span', class_='a-icon-alt')
price = soup.find_all('span', class_='_cDEzb_p13n-sc-price_3mJ9Z')

print(price)
def get_name ():
    for product_name in name:
        tech_product_name.append(product_name.string)
    return tech_product_name
get_name()

def get_rank (): 
    for product_rank in rank:
        tech_product_rank.append(product_rank.string)
    return tech_product_rank
get_rank()

def get_stars ():
    for product_stars in stars:
        tech_product_stars.append(product_stars.string)
    return tech_product_stars
get_stars()

def get_price():
    for product_price in price:
        tech_product_price.append(product_price.string)
    return tech_product_price
get_price()
