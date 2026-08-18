"""
Un equipo de Fórmula 1 registra los nombres de sus 4 pilotos junto con los tiempos (en
segundos) obtenidos en sus últimas 3 vueltas de clasificación.
La estructura de datos debe ser una lista general. Cada elemento de la lista será
una sublista que contenga en el primer componente el nombre del piloto (cadena
de caracteres) y en el segundo componente una tupla con sus 3 tiempos
(flotantes).
 Sugerencia de estructura interna si se cargara por asignación:
pilotos = [ ["Franco", (78.5, 77.2, 79.1)], ["Lewis", (77.9, 78.1, 77.4)], ... ]
Desarrollar las siguientes funciones:
1. Cargar pilotos: Solicitar por teclado el nombre de cada uno de los 4 pilotos y sus
3 mejores tiempos para estructurar la lista y las tuplas correspondientes.
2. Calcular Promedios: Recorrer la estructura de datos, calcular el tiempo promedio
de cada piloto en sus 3 vueltas e imprimir su nombre junto a dicho promedio.
3. Mejor Vuelta: Recorrer la estructura para buscar y mostrar la vuelta más rápida de
toda la clasificación (el tiempo individual más bajo dentro de cualquier tupla),
detallando a qué piloto le pertenece.
"""
def cargar_pilotos():
    pilotos = []
    for i in range(4):
        nombre = input(f"Ingrese el nombre del piloto {i + 1}: ")
        tiempos_lista = []
        for j in range(3):
            tiempo = float(input(f"Ingrese el tiempo de la vuelta {j + 1} para {nombre} (en segundos): "))
            tiempos_lista.append(tiempo)
        tiempos_tupla = (tiempos_lista[0], tiempos_lista[1], tiempos_lista[2])
        pilotos.append([nombre, tiempos_tupla])
        
    return pilotos
def calcular_promedios(pilotos):
    promedios = []
    for piloto in pilotos:
        nombre = piloto[0]
        tiempos = piloto[1]
        suma = 0.0
        for tiempo in tiempos:
            suma = suma + tiempo
        promedio = suma / len(tiempos)
        promedios.append([nombre, promedio])
    return promedios
def buscar_mejor_vuelta(pilotos):
    mejor_tiempo = pilotos[0][1][0]
    piloto_mejor_vuelta = pilotos[0][0]
    
    for piloto in pilotos:
        nombre = piloto[0]
        tiempos = piloto[1]
        for tiempo in tiempos:
            if tiempo < mejor_tiempo:
                mejor_tiempo = tiempo
                piloto_mejor_vuelta = nombre
                
    return piloto_mejor_vuelta, mejor_tiempo
def mostrar_promedios(promedios):
    print("--- TIEMPOS PROMEDIO POR PILOTO ---")
    for reg in promedios:
        print(f"Piloto: {reg[0]} - Tiempo Promedio: {reg[1]} segundos")

def mostrar_mejor_vuelta(nombre, tiempo):
    print("--- MEJOR VUELTA DE LA CLASIFICACION ---")
    print(f"La vuelta mas rapida fue de {tiempo} segundos, lograda por {nombre}.")
datos_pilotos = cargar_pilotos()
promedios_obtenidos = calcular_promedios(datos_pilotos)
mostrar_promedios(promedios_obtenidos)
piloto_rapido, tiempo_rapido = buscar_mejor_vuelta(datos_pilotos)
mostrar_mejor_vuelta(piloto_rapido, tiempo_rapido)