from bs4 import BeautifulSoup
from urllib.request import urlopen
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
import re

file = urlopen("https://dievalhu.github.io/diegovallejo/")
html = file.read()
file.close()

soup = BeautifulSoup(html, 'html.parser')
busca = soup.find_all("a")

tit = []
for links in busca:
    tit.append(links.get('href'))

titulos = tit[1:7]
# print(titulos)

a = "who plays as a forward and captains both Spanish club Barcelona and the Argentina national team. Often considered the best player in the world and widely regarded as one of the greatest players of all time, Messi has won a record six"
n1 = a.lower()
n2 = re.sub('[^A-Za-z0-9]+', ' ', n1)
n3 = n2.split()
print(len(n3))
# nltk.download('stopwords')
n4 = stopwords.words('english')
# print(n4)

for word in n3:
    if word in n4:
        n3.remove(word)

print(n3)
print(len(n3))

stemmer = PorterStemmer()
n5 = stemmer.stem("plays")
n6 = []
for i in n3:
    n6.append(stemmer.stem(i))

print(n6)
