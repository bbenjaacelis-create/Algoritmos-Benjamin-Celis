"""
1. En un curso de 4 alumnos se registraron las notas de sus exámenes y se
deben procesar de acuerdo a lo siguiente:
a. Ingresar nombre y nota de cada alumno (almacenar los datos en
dos listas paralelas)
b. Realizar un listado que muestre los nombres, notas y condición del
alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o
igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente"
si la nota es inferior a 4.
c. Imprimir cuántos alumnos tienen la leyenda “Muy Bueno”.
"""
nombres=[]
notas=[]
mb = 0
for x in range(4):
    nom=input("Ingrese el nombre del alumno: ")
    nombres.append(nom)
    no=int(input(f"Ingrese las notas del alumno: {nom}: "))
    notas.append(no)
for x in range(4):
    if notas [x]>= 8:
        print(f"El alumno {nombres [x]} tiene una calificacion de {notas[x]}, Muy Bueno ")
        mb = mb+1
    elif notas [x] > 4 and notas [x] < 7:
        print(f"El alumno {nombres [x]}, tiene una califiacion de {notas[x]}, Bueno ")
    else:
        print(f"El alumno {nombres [x]}, tiene una nota de {notas[x]}, Insuficiente ")
print(f"Los alumnos con la nota Muy Bueno son {mb}")