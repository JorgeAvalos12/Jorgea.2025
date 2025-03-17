# Definimos una matriz 3x3
def buscar_en_matriz(matriz, valor):
    for a in range(len(matriz)):
        for k in range(len(matriz[a])):
            if matriz[a][k] == valor:
                return (a, k)  
    return None 

matriz = [
    [5, 4, 3],
    [4, 5, 6],
    [7, 8, 9]
]

valor_a_buscar = 9

resultado = buscar_en_matriz(matriz, valor_a_buscar)

if resultado:
    print(f"{valor_a_buscar} se encuentra en la posición {resultado}.")
else:
    print(f"{valor_a_buscar} no se encuentra en la matriz.")