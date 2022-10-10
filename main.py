import requests
from bs4 import BeautifulStoneSoup
import csv

import techProduct
import petSupplies
import dvd

header = ['Nom produit informatique', 'Classement', 'nombre d\'étoiles', 'Titre du film', 'Classement', 'Nombre d\'étoiles', 'Produit animalier', 'Classement', 'Nombre d\'étoiles']
with open('bestSellers-data.csv', 'w', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(header)
    for nom_informatique, classement_informatique, étoiles_informatique, film, classement_film, étoiles_film, nom_produit, classement_produit, étoiles_produits in zip(techProduct.tech_product_name, techProduct.tech_product_rank, techProduct.tech_product_stars, dvd.dvd_name, dvd.dvd_rank, dvd.dvd_stars, petSupplies.supplies_product_name, petSupplies.supplies_product_rank, petSupplies.supplies_product_stars):
        writer.writerow([nom_informatique, classement_informatique, étoiles_informatique, film, classement_film, étoiles_film, nom_produit, classement_produit, étoiles_produits])