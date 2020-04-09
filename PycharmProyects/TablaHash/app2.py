"""
Created on Sun Sep 29 13:18:53 2019
@author: Leonel
"""

palabra = 'supercalifragilisticoespialidoso'
dimension = len(palabra)
contador = 0
template = ''
A = 2

for i, numero in enumerate(palabra):
    dimension = dimension - 1
    fc = ord(numero) * (A ** dimension)
    template = template+f'{ord(numero)}*{A}^{dimension} + '
    contador = contador + fc

print(f'{template[:-3]} = {contador}')
print(f'Total codificado = {contador}')
