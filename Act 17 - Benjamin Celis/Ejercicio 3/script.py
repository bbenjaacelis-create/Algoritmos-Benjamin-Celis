"""
3. Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los
números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltan menos
días.
"""
empleado = []
faltas = []
for x in range(3):
    nombre=input(f"Ingrese el nombre del empleado {x+1}: ")
    empleado.append(nombre)
    dias_str = input(f"Ingrese los dias que falto {nombre} (separados por coma): ")
    dias_lista = dias_str.split(",") 

    sublista = []
    for d in dias_lista:
        sublista.append(int(d))  

    faltas.append(sublista) 

print("Dias que falto cada empleado")

for x in range(3):
    print(f"{empleado[x]} faltó los días: {faltas[x]}")

print("Cantidad de inasistencias de cada empleado")

for x in range(3):
    print(f"{empleado[x]}: {len(faltas[x])} inasistencias")  

menor = len(faltas[0]) 
for x in range(1, 3):
    if len(faltas[x]) < menor:  
        menor = len(faltas[x])  


print("Empleados que faltan menos días")
for x in range(3):
    if len(faltas[x]) == menor:
        print(f"{empleado[x]} con {menor} inasistencias")