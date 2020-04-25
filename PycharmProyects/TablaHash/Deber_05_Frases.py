from bs4 import BeautifulSoup
from urllib.request import urlopen
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import csv
import re


# dependencias:
# import nltk
# nltk.download('stopwords')

def normalizacion(textos):
    for i, texto in enumerate(textos):
        texto = texto.lower()
        texto = re.sub("[^A-Za-z0-9’]+", ' ', texto)
        textos[i] = texto
    return textos


def tokenizacion(textos):
    for i, texto in enumerate(textos):
        textos[i] = texto.strip().split()
    return textos


def deleteStopWords(textos):
    sw = stopwords.words('english')
    for i, texto in enumerate(textos):
        copia = texto[:]
        for palabra in copia:
            if palabra in sw:
                texto.remove(palabra)
    return textos


def stemming(textos):
    stemmer = PorterStemmer()
    for texto in textos:
        for i, palabra in enumerate(texto):
            texto[i] = stemmer.stem(palabra)
    return textos


def crearDiccionario(vector):
    diccionario = []
    for texto in vector:
        for palabra in texto:
            if not palabra in diccionario:
                diccionario.append(palabra)
    return diccionario


def contarOcurrencias(diccionario, vector):
    ocurrencias = []
    for palabraDelDiccionario in diccionario:
        auxOcurrencias = []
        for numeroDeTexto, texto in enumerate(vector):
            aux = []
            ubicaciones = []
            contador = 0
            for ubicacionpalabradelTexto, palabraDelTexto in enumerate(texto):
                if palabraDelDiccionario == palabraDelTexto:
                    contador = contador + 1
                    ubicaciones.append(ubicacionpalabradelTexto + 1)
            if contador > 0:
                aux.append(numeroDeTexto + 1)
                aux.append(contador)
                aux.append(ubicaciones)
                auxOcurrencias.append(aux)

        ocurrencias.append(auxOcurrencias)
    return ocurrencias


file = urlopen("https://www.fearlessmotivation.com/2017/07/19/steve-jobs-quotes/")
html = file.read()
file.close()

soup = BeautifulSoup(html, 'html.parser')
titulos = []
for links in soup.find_all("h2"):
    frase = links.get_text()
    frase = frase[3:len(frase)].strip()
    titulos.append(frase)

titulos = titulos[0:5]
titulos = normalizacion(titulos)
titulos = tokenizacion(titulos)
titulos = deleteStopWords(titulos)
titulos = stemming(titulos)
diccionario = crearDiccionario(titulos)
ocurrencias = contarOcurrencias(diccionario, titulos)
for x in zip(diccionario, ocurrencias):
    print(x)

# myFile = open('headers.csv', 'w')
# with myFile:
#     writer = csv.writer(myFile)
#     for x in titulos:
#         writer.writerow([x])
#
# for x in titulos:
#     print(x)
