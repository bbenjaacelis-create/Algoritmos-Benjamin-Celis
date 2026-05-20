"""
Una empresa registra los nombres de sus 5 vendedores y el total de ventas
realizadas por cada uno en un mes. Cargar los nombres y ventas en dos
vectores paralelos, ordenar los datos de mayor a menor según las ventas,
imprimir la lista ordenada con nombre y monto de la venta, e informar quien fue
el que menos vendió de los 5 empleados.
"""
v=[]
ve=[]
for x in range(5):
    d=input(f"Ingrese el nombre de los vendedor {x+1}° ")
    v.append(d)
    u=int(input(f"Ingrese el total de las ventas del mes de {d}: "))
    ve.append(u)
for e in range(4):
    for j in range(4):
        if ve[j]<ve[j+1]:
            aux1=ve[j]
            ve[j]=ve[j+1]
            ve[j+1]=aux1
            aux2=v[j]
            v[j]=v[j+1]
            v[j+1]=aux2
print("Lista de mayores a menores ventas")
for x in range(5):
    print(v[x], ve[x])
menor=ve[4]
menorcito=v[4]
print(f"El vendedor con la menor venta fue: {menorcito}, con la lamentable cantidad de: {menor} ventas...")
