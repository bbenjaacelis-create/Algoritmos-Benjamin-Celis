"""
Una empresa de e-commerce utiliza drones autónomos para realizar entregas a domicilio
y necesita rastrear las coordenadas geográficas de sus rutas de vuelo.
Diseñar un diccionario donde la Clave sea el identificador único del dron (ej:
"DRON-01") y el Valor sea una lista de tuplas que almacene las coordenadas de
las paradas programadas: [(latitud, longitud)].
Desarrollar las siguientes funciones:
1. Cargar planes de vuelo: Ingresar la información de 3 drones. Solicitar para cada
uno la cantidad de paradas que va a realizar y cargar sus respectivas coordenadas
geográficas.
2. Imprimir rutas: Mostrar el listado completo de los drones junto con sus paradas
de coordenadas asociadas.
3. Ruta más larga: Determinar y mostrar el identificador del dron que tiene la mayor
cantidad de paradas registradas en su ruta de vuelo (la lista con mayor cantidad
de elementos).
"""
def cargar_planes_de_vuelo():
    drones = {}
    for i in range(3):
        id_dron = input("Ingrese el ID del dron (ej: DRON-01): ")
        cant_paradas = int(input(f"Ingrese la cantidad de paradas para {id_dron}: "))
        paradas = []
        for j in range(cant_paradas):
            lat = float(input(f"Ingrese la latitud de la parada {j + 1}: "))
            lng = float(input(f"Ingrese la longitud de la parada {j + 1}: "))
            paradas.append((lat, lng))
        drones[id_dron] = paradas
    return drones

def imprimir_rutas(drones):
    print("--- RUTAS DE VUELO DE DRONES ---")
    for id_dron in drones:
        print(f"Dron: {id_dron}")
        for k in range(len(drones[id_dron])):
            coordenada = drones[id_dron][k]
            print(f"  Parada {k + 1}: Latitud {coordenada[0]}, Longitud {coordenada[1]}")

def ruta_mas_larga(drones):
    print("--- DRON CON LA RUTA MAS LARGA ---")
    max_paradas = -1
    dron_mas_largo = ""
    
    for id_dron in drones:
        cant_paradas = len(drones[id_dron])
        if cant_paradas > max_paradas:
            max_paradas = cant_paradas
            dron_mas_largo = id_dron
            
    if max_paradas >= 0:
        print(f"El dron con la ruta mas larga es '{dron_mas_largo}' con {max_paradas} paradas.")
datos_drones = cargar_planes_de_vuelo()
imprimir_rutas(datos_drones)
ruta_mas_larga(datos_drones)