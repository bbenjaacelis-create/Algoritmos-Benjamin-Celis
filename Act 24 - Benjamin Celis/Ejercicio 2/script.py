"""
En un videojuego multijugador en línea, los jugadores se agrupan en clanes o gremios
para realizar misiones cooperativas.
Diseñar un diccionario donde la Clave sea el nombre del Gremio (ej:
"DragonesDeFuego") y el Valor sea una lista de cadenas con los nombres de
los jugadores (nicknames) que lo integran.
Desarrollar las siguientes funciones:
1. Registrar gremios: Cargar por teclado 3 gremios. Para cada gremio, se debe
preguntar cuántos integrantes posee para cargar sus respectivos nombres de
usuario en la lista interna.
2. Listar clanes: Mostrar los nombres de todos los gremios junto a la cantidad total
de miembros que posee cada uno.
3. Buscar jugador: Solicitar por teclado el nombre de un jugador y buscar en qué
gremio está registrado. Informar el gremio encontrado o indicar si el jugador es
"Solitario" (no pertenece a ningún clan).
"""
def registrar_gremios():
    gremios = {}
    for i in range(3):
        nombre_gremio = input("Ingrese el nombre del gremio: ")
        cant_integrantes = int(input(f"Ingrese la cantidad de integrantes para {nombre_gremio}: "))
        integrantes = []
        for j in range(cant_integrantes):
            jugador = input(f"Ingrese el nombre del jugador {j + 1}: ")
            integrantes.append(jugador)
        gremios[nombre_gremio] = integrantes
    return gremios

def listar_clanes(gremios):
    print("--- LISTADO DE GREMIOS ---")
    for gremio in gremios:
        cantidad = len(gremios[gremio])
        print(f"Gremio: {gremio} - Cantidad de miembros: {cantidad}")

def buscar_jugador(gremios):
    buscado = input("Ingrese el nombre del jugador a buscar: ")
    encontrado = 0
    gremio_encontrado = ""
    
    for gremio in gremios:
        for jugador in gremios[gremio]:
            if jugador == buscado:
                encontrado = 1
                gremio_encontrado = gremio
                
    if encontrado == 1:
        print(f"El jugador {buscado} pertenece al gremio: {gremio_encontrado}")
    else:
        print(f"El jugador {buscado} es Solitario (no pertenece a ningún clan)")

datos_gremios = registrar_gremios()
listar_clanes(datos_gremios)
buscar_jugador(datos_gremios)