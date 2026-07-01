"""
2-
Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea
el número de documento del alumno. Como valor almacenar una lista con
componentes de tipo tupla donde almacenamos nombre de materia y su nota.
Crear las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las
materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.
"""



def carga():
    diccionario={}
    codigo="s"
    for x in range (3):
        documento=int(input(f"ingrese el documento del alumno {x}: "))
        lista=[]
        while codigo=="s":
            nombre=input("ingrese el nombre de su materia: ")
            nota=int(input(f"ingrese la nota de {nombre} que tuvo el alumno: "))
            lista.append((nombre, nota))
            codigo=input("desea agregar otra materia? (s/n): ")
        diccionario[documento]=lista
        codigo="s"    
    return diccionario


def entera(lista):
    print("LISTA COMPLETA: ")
    print(lista)



def consulta(lista):
    valor=int(input("ingrese el numero de documento: "))
    if valor in lista:
        print(lista[valor])


lista=carga()
entera(lista)
consulta(lista)