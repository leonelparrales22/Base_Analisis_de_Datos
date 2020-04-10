dimension = 5
vector = [12, 14, 78, 90, 10]

tabla = [-1] * dimension
print('CON COLISIONES')

for x in range(0, len(vector)):
    hx = vector[x] % dimension
    print(f'VECTOR[{x}]={vector[x]}-->{hx}')
    if tabla[hx] == -1:
        tabla[hx] = vector[x]
    else:
        kx = (vector[x] % (dimension - 1)) + 1
        h = hx
        bandera = True
        while bandera:
            h = (h + kx) % dimension
            if tabla[h] == -1:
                tabla[h] = vector[x]
                bandera = False

print('\nSIN COLISIONES:')
for i, numero in enumerate(tabla):
    if numero == -1:
        numero = ""
    print(f'HashTable[{i}]: {numero}')
