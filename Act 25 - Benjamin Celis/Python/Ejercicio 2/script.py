"""
Para un sistema de radares de tránsito, se necesita registrar la ubicación geográfica de 4
cámaras de control.
Almacenar en una lista las coordenadas de las 4 cámaras. Cada elemento de la
lista debe ser una tupla de dos flotantes (latitud, longitud) ingresados por teclado.
Desarrollar las siguientes funciones:
1. Cargar coordenadas: Solicitar la latitud y la longitud de cada una de las 4
cámaras para armar las tuplas y agregarlas a la lista.
2. Listar posiciones: Recibir la lista e imprimir las coordenadas de todas las
cámaras. Importante: Realizar el recorrido utilizando un bucle for que
desempaquete la tupla directamente en las variables lat y lon en cada vuelta (sin
utilizar índices numéricos como [0] o [1]).
3. Filtrar hemisferio: Contar e informar cuántas de las cámaras se encuentran
ubicadas en el hemisferio norte (latitud mayor a cero).
"""
def cargar_coordenadas():
    camaras = []
    for i in range(4):
        lat = float(input(f"Ingrese la latitud de la camara {i + 1}: "))
        lon = float(input(f"Ingrese la longitud de la camara {i + 1}: "))
        camaras.append((lat, lon))
    return camaras

def listar_posiciones(camaras):
    print("--- POSICIONES DE LAS CAMARAS ---")
    i = 1
    for lat, lon in camaras:
        print(f"Camara {i}: Latitud {lat}, Longitud {lon}")
        i = i + 1

def contar_hemisferio_norte(camaras):
    contador = 0
    for lat, lon in camaras:
        if lat > 0:
            contador = contador + 1
    return contador

def mostrar_reporte_hemisferio(cantidad_norte):
    print("--- REPORTE DE HEMISFERIO ---")
    print(f"Cantidad de camaras en el hemisferio norte: {cantidad_norte}")


lista_camaras = cargar_coordenadas()
listar_posiciones(lista_camaras)
norte_cant = contar_hemisferio_norte(lista_camaras)
mostrar_reporte_hemisferio(norte_cant)