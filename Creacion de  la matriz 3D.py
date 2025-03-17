#Definimos la matriz 3D
#Dimensiones: [ciudades][semanas][días de la semana]
#Tenemos 3 ciudades, Quito, Cuenca, Guayaquil, 4 semanas y 7 días de la semana
temperaturas = [
    [  # Quito 
        [30, 31, 29, 28, 32, 30, 31],  # Semana 1
        [29, 30, 31, 32, 30, 29, 28],  # Semana 2
        [31, 32, 30, 29, 28, 30, 31],  # Semana 3
        [30, 29, 28, 31, 32, 30, 29]   # Semana 4
    ],
    [  # Cuenca
        [25, 26, 27, 28, 29, 30, 31],  # Semana 1
        [26, 27, 28, 29, 30, 31, 32],  # Semana 2
        [27, 28, 29, 30, 31, 32, 33],  # Semana 3
        [28, 29, 30, 31, 32, 33, 34]   # Semana 4
    ],
    [  # Guayaquil
        [20, 21, 22, 23, 24, 25, 26],  # Semana 1
        [21, 22, 23, 24, 25, 26, 27],  # Semana 2
        [22, 23, 24, 25, 26, 27, 28],  # Semana 3
        [23, 24, 25, 26, 27, 28, 29]   # Semana 4
    ]
]

# Nombres de las ciudades
nombres_ciudades = ["Quito", "Cuenca", "Guayaquil"]

# Calcular y mostrar el promedio de temperaturas
for Q in range(len(temperaturas)):  
    for C in range(len(temperaturas[Q])): 
        suma_temperaturas = 0
        for G in range(len(temperaturas[Q][C])): 
            suma_temperaturas += temperaturas[Q][C][G]
        
        promedio = suma_temperaturas / len(temperaturas[Q][C])
        print(f"Promedio de temperaturas para {nombres_ciudades[Q]} en la semana {C + 1}: {promedio:.2f}°C")
        
        
        
#Se explica el propósito de cada bucle anidado:
#El primer bucle actua sobre las ciudades.
#El segundo bucle actua sobre las semanas de la ciudad actual.
#El tercer bucle actua sobre los días de la semana actual.
        