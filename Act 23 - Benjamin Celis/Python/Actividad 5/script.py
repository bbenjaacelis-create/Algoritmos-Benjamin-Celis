"""
Ejercicio 5: Gestión de Triaje en Guardia Médica (Prioridad)
Contexto: Un hospital atiende pacientes según la gravedad de su condición (Triaje), no
únicamente por orden de llegada. Los niveles de urgencia son: 1 (Normal), 2 (Moderado) y 3
(Crítico).
Consigna: La sala de espera se representa como una lista de registros sin diccionarios:
[["Paciente", Prioridad], ...]. Crear la función atender_siguiente(cola_espera) que seleccione
al próximo paciente en ser atendido.
Requisitos:
● Buscar al paciente que posea la prioridad más alta (mayor número).
● En caso de empate en la prioridad, se debe atender al primero que haya llegado a
la guardia (criterio FIFO).
● Eliminar al paciente seleccionado de la lista de espera y devolver un mensaje
indicando su nombre y nivel de urgencia.
Ejemplo de Entrada: [["Carlos", 1], ["Ana", 3], ["Roberto", 2], ["Lucía", 3]] Salida
Esperada: Atiende primero a Ana (Nivel 3). Si se vuelve a llamar a la función,
la siguiente será Lucía (Nivel 3).
"""
def cargar_pacientes():
    cola_espera = []
    cant = int(input("Ingrese la cantidad de pacientes en espera: "))
    
    for i in range(cant):
        nombre = input("Nombre del paciente: ")
        prioridad = int(input("Prioridad (1=Normal, 2=Moderado, 3=Critico): "))
        cola_espera.append([nombre, prioridad])
        
    return cola_espera

def atender_siguiente(cola_espera):
    if len(cola_espera) == 0:
        print("No hay pacientes en la cola de espera.")
        return
    
    posicion_maxima = 0
    maxima_prioridad = cola_espera[0][1]
    
    for i in range(1, len(cola_espera)):
        if cola_espera[i][1] > maxima_prioridad:
            maxima_prioridad = cola_espera[i][1]
            posicion_maxima = i
        
    paciente = cola_espera.pop(posicion_maxima)
    
    print(f"Atiende a {paciente[0]} (Nivel {paciente[1]})")
cola = cargar_pacientes()

print("--- Atendiendo pacientes ---")
cant_a_atender = len(cola)
for i in range(cant_a_atender):
    atender_siguiente(cola)