"""
Ejercicio 1: Sistema de Reserva de Butacas (Matrices 2D)
Contexto: Un cine necesita un módulo automatizado para vender entradas. La sala se
representa como una matriz (lista de listas) de N filas por M columnas, donde un 0
representa un asiento libre y un 1 uno ocupado.
Consigna:
Escribir una función llamada reservar_consecutivos(sala, fila, cantidad) que reciba la matriz
de la sala, el número de fila deseado y la cantidad de entradas que desea comprar el grupo
de clientes.
Requisitos:
● Debe buscar si existen suficientes asientos libres y contiguos (juntos) en esa
misma fila.
● Si los encuentra, debe cambiar sus valores a 1 (ocupados) y retornar un mensaje
confirmando la reserva con los números de columna asignados.
● Si no hay espacio consecutivo suficiente, debe indicar que no fue posible realizar la
reserva sin modificar la sala.
Ejemplo de Entrada:
Sala de 3x5. En la fila 0, la columna 1 ya está ocupada: [ [0, 1, 0, 0, 0], ... ]
Intentar reservar 3 asientos en la fila 0.
Salida Esperada: Confirmación de reserva para las columnas 2, 3 y 4.
"""
def mostrar_sala(sala):
    print("[")
    for fila in sala:
        print(f"  {fila},")
    print("]")

def reservar_consecutivos(sala, fila, cantidad):
    columnas_fila = len(sala[fila])
    libres_seguidos = 0
    col_inicio = -1
    col = 0
    
    while col < columnas_fila and libres_seguidos < cantidad:
        if sala[fila][col] == 0:
            if libres_seguidos == 0:
                col_inicio = col
            libres_seguidos += 1
        else:
            libres_seguidos = 0
        col += 1
            
    if libres_seguidos == cantidad:
        columnas_reservadas = []
        for c in range(col_inicio, col_inicio + cantidad):
            sala[fila][c] = 1
            columnas_reservadas.append(c)
        print(f"Reserva exitosa en la fila {fila}. Columnas asignadas: {columnas_reservadas}")
    else:
        print(f"No fue posible realizar la reserva: no hay {cantidad} asientos consecutivos libres.")

filas = int(input("Ingrese cantidad de filas de la sala: "))
cols = int(input("Ingrese cantidad de columnas de la sala: "))

sala = []
print("--- Carga de la Sala (0 = Libre, 1 = Ocupado) ---")
for i in range(filas):
    fila_actual = []
    for j in range(cols):
        estado = int(input(f"Estado del asiento [Fila {i}, Columna {j}]: "))
        fila_actual.append(estado)
    sala.append(fila_actual)

print("Sala inicial cargada:")
mostrar_sala(sala)

print("--- Solicitud de Reserva ---")
f_deseada = int(input("Ingrese la fila donde desea reservar: "))
cant_deseada = int(input("Ingrese la cantidad de asientos a reservar: "))

reservar_consecutivos(sala, f_deseada, cant_deseada)

print("Estado final de la sala:")
mostrar_sala(sala)