def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return True, i, j
    return False, -1, -1

# Crear matriz 3x3
matriz = [
    [5, 2, 9],
    [1, 8, 3],
    [4, 7, 6]
]

# Valor a buscar
valor_buscado = 8

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Realizar búsqueda
encontrado, fila, columna = buscar_valor(matriz, valor_buscado)

# Mostrar resultado
if encontrado:
    print(f"\nEl valor {valor_buscado} se encontró en la posición [{fila}][{columna}]")
else:
    print(f"\nEl valor {valor_buscado} no se encontró en la matriz")