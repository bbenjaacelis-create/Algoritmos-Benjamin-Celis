"""
Un sistema de hogar inteligente monitorea qué electrodomésticos consumen más energía
en cada habitación de la casa.
Crear un diccionario donde la Clave sea el nombre del ambiente (ej: "Cocina",
"Dormitorio") y el Valor sea una lista de tuplas, donde cada tupla represente un
dispositivo activo y su consumo: [(nombre_dispositivo, consumo_watts)].
Desarrollar las siguientes funciones:
1. Cargar dispositivos: Solicitar la carga de 3 habitaciones. Para cada habitación,
ingresar el nombre de los dispositivos activos y su consumo en Watts hasta que el
operador decida no cargar más para ese ambiente.
2. Consumo por habitación: Imprimir el listado de habitaciones y el consumo total
en Watts acumulado en cada una de ellas.
3. Dispositivo crítico: Buscar e informar el nombre del electrodoméstico que más
energía consume de toda la casa (el valor máximo individual dentro de todas las
listas del diccionario), indicando en qué habitación se encuentra.
"""
def cargar_dispositivos():
    ambientes = {}
    for i in range(3):
        habitacion = input("Ingrese el nombre de la habitacion: ")
        dispositivos = []
        continuar = "s"
        while continuar == "s" or continuar == "S":
            nombre_disp = input(f"Ingrese el nombre del dispositivo para {habitacion}: ")
            consumo_watts = float(input(f"Ingrese el consumo en Watts de {nombre_disp}: "))
            dispositivos.append((nombre_disp, consumo_watts))
            continuar = input("¿Desea ingresar otro dispositivo en esta habitacion? (s/n): ")
        ambientes[habitacion] = dispositivos
    return ambientes

def consumo_por_habitacion(ambientes):
    print("--- CONSUMO TOTAL POR HABITACION ---")
    for habitacion in ambientes:
        total_watts = 0.0
        for disp in ambientes[habitacion]:
            total_watts = total_watts + disp[1]
        print(f"Habitacion: {habitacion} - Consumo Total: {total_watts} W")

def dispositivo_critico(ambientes):
    print("--- DISPOSITIVO DE MAYOR CONSUMO ---")
    max_consumo = -1.0
    disp_critico = ""
    hab_critica = ""
    
    for habitacion in ambientes:
        for disp in ambientes[habitacion]:
            nombre = disp[0]
            consumo = disp[1]
            if consumo > max_consumo:
                max_consumo = consumo
                disp_critico = nombre
                hab_critica = habitacion
                
    if max_consumo >= 0:
        print(f"El dispositivo critico es '{disp_critico}' con {max_consumo} W en la habitacion '{hab_critica}'.")
datos_ambientes = cargar_dispositivos()
consumo_por_habitacion(datos_ambientes)
dispositivo_critico(datos_ambientes)