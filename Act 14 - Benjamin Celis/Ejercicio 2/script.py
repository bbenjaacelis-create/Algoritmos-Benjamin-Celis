"""
2. Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8
empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa
que permita almacenar los sueldos de los empleados agrupados en dos
listas. Imprimir las dos listas de sueldos.
"""
em= []
et = []

for x in range(4):
    sueldo = int(input(f"Ingrese el sueldo del empleado {x+1} de la mañana:"))
    em.append(sueldo)

for x in range(4):
    sueldo = int(input(f"Ingrese el sueldo del empleado {x+1} de la tarde:"))
    et.append(sueldo)

print("Lista de empleados de la mañana")
print(em)
print("Lista de empleados de la tarde")
print(et)