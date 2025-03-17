#Se debe calcular la temperatura promnedio de una diferentes ciudades
#calcular el perioda de tiempo en semanas 

def calcular_temperatura_promedio(ciudades, semanas_temperaturas):
    promedios = {ciudad: 0 for ciudad in ciudades}
    total_dias = len(semanas_temperaturas) * 7  

    
    for semana in semanas_temperaturas:
        for i, ciudad in enumerate(ciudades):
            
            promedios[ciudad] += sum(semana[i])

    
    for ciudad in promedios:
        promedios[ciudad] /= total_dias

    return promedios

def ingresar_datos(ciudades, semanas):
   
    semanas_temperaturas = []
    for semana_num in range(semanas):
        print(f"\nIngrese las temperaturas para la Semana {semana_num + 1}:")
        semana = []
        for dia in range(7):  
            temperaturas_dia = []
            for ciudad in ciudades:
                while True:
                    try:
                        temperatura = float(input(f"Ingrese la temperatura de {ciudad} para el día {dia + 1}: "))
                        temperaturas_dia.append(temperatura)
                        break  
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
            semana.append(temperaturas_dia)
        semanas_temperaturas.append(semana)
    return semanas_temperaturas

def mostrar_resultados(resultados):
    print("\nResultados de temperatura promedio:")
    for ciudad, promedio in resultados.items():
        print(f"La temperatura promedio en {ciudad} es: {promedio:.2f}°C")


ciudades = ["Loja","Esmeraldas","Riobamba","Quito","Salinas"]
semanas = 3


semanas_temperaturas = ingresar_datos(ciudades, semanas)


resultados = calcular_temperatura_promedio(ciudades, semanas_temperaturas)
mostrar_resultados(resultados)

#Esta función tiene una lista de ciudades y una lista de temperaturas organizadas por semanas.
#Tiene  promedios para almacenar la suma de las temperaturas de cada ciudad.
#Calcula el total de días multiplicando el número de semanas por 7.
#Repite el codigo sobre cada semana y cada ciudad, sumando las temperaturas.
#Finalmente calcula el promedio dividiendo la suma total de temperaturas por el