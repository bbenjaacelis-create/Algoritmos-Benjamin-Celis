"""
2. En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio.
"""

def cargar():
    li=[]
    for x in range(10):
        pedir=int(input(f"Ingrese el {x+1}° sueldo: "))
        li.append(pedir)
    return li

def cargar_sueldos(li):
    print("----TODOS LOS SUELDOS----")
    for x in li:
        print(x)

def mayor4000(li):
    print("-----SUELDOS MAYORES A $4000----")
    for x in range(len(li)):
        if li[x]>4000:
            print(li[x])
def promedio(li):
    print("----PROMEDIO-----")
    suma=0
    for x in range(len(li)):
        suma=suma+li[x]
    pro=suma//10
    print(pro)
    return pro
def sueldo_debajo_promedio(li, pro):
    print("----SUELDOS POR DEBAJO DEL PROMEDIO----")
    for x in range(len(li)):
        if li[x]<pro:
            print(li[x])

lista=cargar()
cargar_sueldos(lista)
mayor4000(lista)
prom=promedio(lista)
sueldo_debajo_promedio(lista, prom)