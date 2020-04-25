from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

file = urlopen("https://www.elcomercio.com/ultima-hora")
html = file.read()
file.close()

soup = BeautifulSoup(html, 'html.parser')
titulos = []
for links in soup.find_all("div", {"class": "listing-title"}):
    titulos.append(links.get_text().strip())

titulos = titulos[0:5]
# for x in titulos:
#    print(x)


myFile = open('headers.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    for x in titulos:
        writer.writerow([x])

for x in titulos:
    print(x)