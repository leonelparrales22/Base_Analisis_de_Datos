import re

vector = ['To do is to be. To be is to do.', 'To be or not to be. I am what I am.',
          'I think therefore I am. Do be do be do.', 'Do do do, da da da. Let it be, let it be.']

# LIMPIANDO LA DATA
for i, texto in enumerate(vector):
    texto = texto.lower()
    texto = re.sub('[^A-Za-z0-9]+', ' ', texto)
    vector[i] = texto

# CREANDO EL DICCIONARIO
diccionario = []
for texto in vector:
    texto = texto.strip()
    texto = texto.split(' ')
    for palabra in texto:
        if not palabra in diccionario:
            diccionario.append(palabra)

# OCURRRENCIAS
ocurrencias = []

for palabraDelDiccionario in diccionario:
    auxOcurrencias = []
    for numeroDeTexto, texto in enumerate(vector):
        aux = []
        ubicaciones = []
        contador = 0
        texto = texto.split(' ')
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

# IMPRESIÓN EN PARNTALLA
for x in ocurrencias:
    print(x)
