"""
Se realiza una evaluación a 6 docentes por parte de sus alumnos. Se registran
sus nombres y puntajes promedio obtenidos (de 1 a 10).
Cargar sus datos en vectores paralelos, mostrar docente con calificación más
alta y más baja, ordenar los vectores de mayor a menor de acuerdo con la
calificación y mostrar en pantalla la cantidad de docentes que aprobaron y
desaprobaron (tomando como base que se aprueba con una nota mayor o
igual a 6)
"""
docentes=[]
puntajes=[]
aprobado=6
for x in range(6):
    i=input(f"Nombre del docente {x+1}: ")
    docentes.append(i)
    c=int(input(f"Ingrese el puntaje que se saco {i}: "))
    puntajes.append(c)
for x in range(5):
    for u in range(5-x):
        if puntajes[u]<puntajes[u+1]:
            aux1=puntajes[u]
            puntajes[u]=puntajes[u+1]
            puntajes[u+1]=aux1
            aux2=docentes[u]
            docentes[u]=docentes[u+1]
            docentes[u+1]=aux2
for x in range(6):
    print(docentes[x], puntajes[x])
print("---PUNTAJE DE DOCENTE MAYOR A MENOR----")
print(f"El docente con la calificacion mas alta: {docentes[0]}")
print(f"El docente con la calificacion mas baja: {docentes[5]}")
for x in range(6):
    if puntajes[x]>=aprobado:
        print(f"{docentes[x]}, esta aprobado")
    else:
        print(f"{docentes[x]}, esta desaprobado")