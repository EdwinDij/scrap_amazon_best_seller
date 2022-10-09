import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.fr/gp/bestsellers/dvd"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

name = soup.find_all('div', class_='_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y')
stars = soup.find_all('span', class_='a-icon-alt')
rank = soup.find_all('span', class_='zg-bdg-text')
bluray_dvd = soup.find_all('span', class_='a-size-small a-color-secondary a-text-normal')

dvd_name = []
dvd_rank = []
dvd_stars = []
dvd_type = []

def get_name ():
    for product_name in name:
        dvd_name.append(product_name.string)
    return dvd_name
get_name()

def get_rank ():
    for product_rank in rank:
        dvd_rank.append(product_rank.string)
    return dvd_rank
get_rank()

def get_stars ():
    for product_stars in stars:
        dvd_stars.append(product_stars.string)
    return dvd_stars
get_stars()

def get_type ():
    for product_type in bluray_dvd:
        dvd_type.append(product_type.string)
    return dvd_type
get_type()
