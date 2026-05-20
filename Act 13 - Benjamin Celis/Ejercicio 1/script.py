"""
1. En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos
empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el
programa deberá informar el importe que gasta la empresa en sueldos al personal.
"""
cienytrescientos = 0
mas300 = 0
suma = 0
empleados = int(input("De cuantos empleados deseas saber su sueldo?"))
for a in range (empleados):
    pedir = int(input("Ingrese los sueldos de cada uno: "))
    if pedir > 100 and pedir < 300:
        print("Usuario que cobra entre 100 y 300")
        cienytrescientos = cienytrescientos + 1
        suma = suma+pedir 
    elif pedir > 300:
        print("Usuario que cobra mas de 300")
        mas300 = mas300 + 1
        suma = suma+pedir 
    
print("----------CANTIDAD DE EMPLEADOS QUE COBRAN ENTRE 100 Y 300---------")
print(cienytrescientos)
print("----------CANTIDAD DE EMPLEADOS QUE COBRAN MAS DE 300---------")
print(mas300)
print("TOTAL QUE GASTA LA EMPRESA EN VALOR DE SUELDOS")
print(suma)