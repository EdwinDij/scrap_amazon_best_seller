import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.fr/gp/bestsellers/dvd"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

dvd_name = soup.find_all('div', class_='_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y')
dvd_stars = soup.find_all('span', class_='a-icon-alt')
dvd_rank = soup.find_all('span', class_='zg-bdg-text')

dvd_name = []
dvd_rank = []
dvd_stars = []

def get_name ():
    for product_name in dvd_name:
        dvd_name.append(product_name.string)
    return dvd_name
get_name()

def get_rank ():
    for product_rank in dvd_name:
        dvd_rank.append(product_rank.string)
    return dvd_rank
get_rank()

def get_stars ():
    for product_stars in dvd_stars:
        dvd_stars.append(product_stars.string)
    return dvd_stars
get_stars()

print(dvd_name)