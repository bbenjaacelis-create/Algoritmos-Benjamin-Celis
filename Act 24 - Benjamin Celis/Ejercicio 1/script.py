"""
1-
Una ciudad inteligente cuenta con sensores que miden las partículas contaminantes de
dióxido de carbono (CO2) en diferentes puntos geográficos.
 Crear un diccionario donde la Clave sea el nombre del barrio o estación de
monitoreo (ej: "San Telmo") y el Valor sea una lista de flotantes que represente
las últimas 3 lecturas de contaminación tomadas en el día.
Desarrollar las siguientes funciones:
1. Cargar sensores: Ingresar por teclado 3 estaciones de monitoreo y, para cada
una, solicitar las 3 lecturas consecutivas de CO2 (en partes por millón - ppm).
2. Reportar promedios: Calcular y mostrar el promedio de contaminación de cada
barrio.
3. Alerta ambiental: Mostrar en pantalla una alerta roja de "Protocolo de
Emergencia" únicamente para las estaciones cuyo promedio de contaminación
supere las 400 ppm.
"""
def cargar_sensores():
    sensores = {}
    for i in range(3):
        barrio = input("Ingrese el nombre del barrio o estacion: ")
        lecturas = []
        for j in range(3):
            lectura = float(input(f"Ingrese la lectura {j + 1} de CO2 (ppm): "))
            lecturas.append(lectura)
        sensores[barrio] = lecturas
    return sensores

def reportar_promedios(sensores):
    promedios = {}
    print("--- Promedios de Contaminacion ---")
    for barrio in sensores:
        suma = 0.0
        for lectura in sensores[barrio]:
            suma = suma + lectura
        promedio = suma / len(sensores[barrio])
        promedios[barrio] = promedio
        print(f"Barrio: {barrio} - Promedio: {promedio} ppm")
    return promedios

def alerta_ambiental(promedios):
    print("--- Alertas Ambientales ---")
    supera_limite = 0
    for barrio in promedios:
        if promedios[barrio] > 400:
            print(f"ALERTA ROJA: Protocolo de Emergencia activado en {barrio} (Promedio: {promedios[barrio]} ppm)")
            supera_limite = supera_limite + 1
            
    if supera_limite == 0:
        print("Todas las estaciones estan dentro de los niveles normales.")

datos_sensores = cargar_sensores()
promedios_obtenidos = reportar_promedios(datos_sensores)
alerta_ambiental(promedios_obtenidos)