"""
Created on Sun Sep 29 13:18:53 2019
@author: Leonel
"""
from random import randint

dimension = int(input("Ingrese tamaño de tabla hash: "))
vector = []

###########################################
##########CREANDO LISTA ALEATORIA##########
###########################################

for x in range(0, dimension):
    bandera = True
    while bandera:
        aleatorio = randint(1, dimension + 100)
        if not aleatorio in vector:
            vector.append(aleatorio)
            bandera = False

for i, numero in enumerate(vector):
    print(f'Ramdon[{i}]: {numero}')

###########################################
###########ASIGNANDO A MEMORIA#############
###########################################
tabla = [-1] * dimension

for x in range(0, dimension):
    hx = vector[x] % dimension
    print(f'{vector[x]}-->{hx}')
    if tabla[hx] == -1:
        tabla[hx] = vector[x]
    else:
        kx = (vector[x] % (dimension - 1)) + 1
        h = hx
        bandera = True
        while bandera:
            print(h)
            print(f'Mi k:{kx}')
            h = (h + kx) % dimension
            if tabla[h] == -1:
                print('VA A IR EN: ', h)
                tabla[h] = vector[x]
                bandera = False

print('SIN COLISIONES:')
for i, numero in enumerate(tabla):
    print(f'HashTable[{i}]: {numero}')






