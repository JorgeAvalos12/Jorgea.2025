## ordenacion_matriz.py

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

def ordenar_fila_matriz(matriz, fila_a_ordenar):
    if fila_a_ordenar < len(matriz):
        print("Matriz original:")
        for fila in matriz:
            print(fila)

        bubble_sort(matriz[fila_a_ordenar])

        print("\nMatriz después de ordenar la fila:")
        for fila in matriz:
            print(fila)
    else:
        print("La fila especificada no existe en la matriz.")


matriz = [
    [12, 5, 3],
    [9, 15, 6],
    [7, 8, 1]
]


ordenar_fila_matriz(matriz, 2)