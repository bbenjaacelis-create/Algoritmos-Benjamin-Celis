"""
3. Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear
y cargar una lista con todos los sueldos de dichos empleados. Imprimir la
lista de sueldos ordenamos de menor a mayor.
"""
em=[]
sue=[]

e=int(input("¿Cuantos empleados tiene la empresa?: "))
for x in range(e):
    r=input(f"Ingrese el nombre del {x+1}° empleado: ")
    em.append(r)
    s=int(input(f"Ingrese el sueldo del {x+1}° empleado: "))
    sue.append(s)
print("Sueldos de cada empleado")
for x in range(e):
    print(f"{em[x]} ----- sueldo: {sue[x]}")
for x in range(e-1):
    if sue[x]<sue[x+1]:
        aux=sue[x]
        sue[x]=sue[x+1]
        sue[x+1]=aux
print("Sueldos de mayor a menor")
print(sue)