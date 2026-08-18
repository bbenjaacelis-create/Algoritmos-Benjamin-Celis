"""
Confeccionar un programa que permita registrar las temperaturas máximas de las últimas
6 horas en una lista.
Desarrollar las siguientes funciones:
1. Carga: Solicitar al operador el ingreso por teclado de las 6 temperaturas y
almacenarlas en una lista.
2. Procesar Extremos: Recibir la lista como parámetro y retornar una tupla que
contenga en su primer componente el valor máximo y en el segundo el valor
mínimo.
3. Bloque Principal: Desempaquetar la tupla devuelta por la función anterior en dos
variables individuales (máxima y mínima) y mostrarlas en pantalla con un mensaje
descriptivo.
"""
def cargar_temperaturas():
    temperaturas = []
    for i in range(6):
        temp = float(input(f"Ingrese la temperatura de la hora {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def procesar_extremos(temperaturas):
    maxima = temperaturas[0]
    minima = temperaturas[0]
    
    for i in range(1, len(temperaturas)):
        if temperaturas[i] > maxima:
            maxima = temperaturas[i]
        if temperaturas[i] < minima:
            minima = temperaturas[i]
            
    return maxima, minima

lista_temps = cargar_temperaturas()
maxima, minima = procesar_extremos(lista_temps)

print(f"La temperatura maxima registrada fue de {maxima} grados.")
print(f"La temperatura minima registrada fue de {minima} grados.")