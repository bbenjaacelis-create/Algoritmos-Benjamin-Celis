"""
Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista
con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en
una tupla)
El programa debe tener las siguientes funciones:
1)Carga de los nombres de empleados y sus últimos tres sueldos.
2)Imprimir el monto total cobrado por cada empleado.
3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a
10000 en los últimos tres meses.
Tener en cuenta que la estructura de datos si se carga por asignación debería ser
similar a:
empleados = [[juan,(2000,3000,4233)] , [ana,(3444,1000,5333)] , etc. ]
"""
def cargar_valores():
    empleados=[]
    for x in range(5):
        nom=input(f"Ingrese el nombre del empleado {x+1}: ")
        sue1=int(input(f"Ingrese el primer sueldo del empleado {nom}: "))
        sue2=int(input(f"Ingrese el primer sueldo del empleado {nom}: "))
        sue3=int(input(f"Ingrese el primer sueldo del empleado {nom}: "))
        empleados.append((nom,sue1,sue2,sue3))
    return empleados

def monto_total(empleados):
    suma=[]
    for x in range(5):
        su=empleados[x][1]+empleados[x][2]+empleados[x][3]
        suma.append(su)
    return suma

def imprimir(empleados,suma):
    print("--LISTA DE EMPLEADOS Y SUELDOS--")
    for x in range(5):
        print(f"El empleado {empleados[x][0]} tiene un sueldo trimestral de {suma[x]}")


def mayores10000(empleados,suma):
    print("--SUELDOS MAYORES A 10000--")
    pos=0
    for x in range(5):
        if suma[x]>10000:
            pos=x
            print(f"El empleado {empleados[pos][0]} tiene sueldo trimestral superior a 10000")
        elif suma[x]<10000:
            pos=0
empleados=cargar_valores()
suma=monto_total(empleados)
imprimir(empleados,suma)
mayores10000(empleados,suma)