"""
Se desea desarrollar un programa que permita registrar los nombres y las
calificaciones de 6 estudiantes. Luego de cargar los datos, se debe mostrar el
nombre del estudiante con la nota más alta, junto con su nota. Al igual que el
estudiante con la nota más baja. Informar si hay estudiantes con la misma nota
máxima o mínima.
"""

nombres=[]
calificaciones=[]
contmax=0
contmin=0
for x in range(6):
    nom=input(f"Ingrese el nombre del {x+1}° alumno: ")
    nombres.append(nom)
    cali=int(input(f"Ingrese la calificacion de {nom}: "))
    calificaciones.append(cali)
for j in range(5):
    for k in range(5-j):
        if calificaciones[k]<calificaciones[k+1]:
            aux1=calificaciones[k]
            calificaciones[k]=calificaciones[k+1]
            calificaciones[k+1]=aux1 
            aux2=nombres[k]
            nombres[k] = nombres[k+1]
            nombres[k+1]=aux2
for x in range(6):
    print(nombres[x], calificaciones[x]) 
minimo = calificaciones [5]
maximo = calificaciones [0]  
for x in range(6):
    if calificaciones[x] == maximo:
        contmax = contmax+1
    elif calificaciones[x] == minimo:
        contmin = contmin+1
if maximo > 1:
    print(f"Alumnos con calificaciones mayores iguales: {contmax}")
if minimo > 1:
    print(f"Alumnos con calificaciones minimas iguales {contmin}")
    