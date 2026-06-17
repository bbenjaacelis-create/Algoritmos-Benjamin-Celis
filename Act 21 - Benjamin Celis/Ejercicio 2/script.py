"""
2-
Confeccionar un programa con las siguientes funciones:
1)Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos
valores
2)Una función que reciba como parámetro dos tuplas con los nombres y sueldos
de empleados y muestre el nombre del empleado con sueldo mayor.
En el bloque principal del programa llamar dos veces a la función de carga y
seguidamente llamar a la función que muestra el nombre de empleado con sueldo
mayor.
# bloque principal
empleado1=cargar_empleado()
empleado2=cargar_empleado()
mayor_sueldo(empleado1,empleado2)
"""

def cargar_empleado():
    empleados_1=[]
    empleados_2=[]
    for x in range (1):
        emp=input(f"ingrese el nombre del empleado: ")
        sue=int(input(f"ingrese el sueldo del empleado {emp}: "))
        emp2=emp=input(f"ingrese el nombre del empleado: ")
        sue2=int(input(f"ingrese el sueldo del empleado {emp2}: "))
        empleados_1.append((emp,sue))
        empleados_2.append((emp2,sue2))
    return empleados_1 and empleados_2

def empleado_mayor(empleados_1,empleados_2):
    pos=0
    for x in range(1):
        if empleados_1[x][1]>empleados_2[pos][1]:
            pos=x
            print("el empleado con mayor sueldo es : ",empleados_1[pos][0] ,"con " ,empleados_1[pos][1])
        elif empleados_1[x][1]<empleados_2[pos][1]:
            pos=x
            print("el empleado con mayor sueldo es : ",empleados_2[pos][0] ,"con " ,empleados_2[pos][1])




empleados_1=cargar_empleado()
empleados_2=cargar_empleado()
empleado_mayor(empleados_1,empleados_2)
