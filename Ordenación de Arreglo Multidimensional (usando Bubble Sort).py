def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]
    return fila

def ordenar_fila_matriz(matriz, fila_a_ordenar):
    matriz_resultado = [fila[:] for fila in matriz]  # Copia de la matriz original
    matriz_resultado[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])
    return matriz_resultado

# Crear matriz 3x3
matriz = [
    [5, 2, 9],
    [1, 8, 3],
    [4, 7, 6]
]

# Fila a ordenar (0, 1 o 2)
fila_seleccionada = 1

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar fila específica
matriz_ordenada = ordenar_fila_matriz(matriz, fila_seleccionada)

# Mostrar matriz con fila ordenada
print(f"\nMatriz con fila {fila_seleccionada} ordenada:")
for fila in matriz_ordenada:
    print(fila)