import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.fr/gp/bestsellers/dvd"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

dvd_name = soup.find_all('div', class_='_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y')
dvd_stars = soup.find_all('span', class_='a-icon-alt')
dvd_rank = soup.find_all('span', class_='zg-bdg-text')