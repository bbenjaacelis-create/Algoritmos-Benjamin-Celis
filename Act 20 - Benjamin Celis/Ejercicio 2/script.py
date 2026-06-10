"""
Desarrollar una aplicación que permita ingresar por teclado los nombres de
5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de artículos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con
un precio menor igual al valor ingresado.
"""

def cargar():
    nombres=[]
    precios=[]
    for x in range(5):
        n=input(f"Ingrese el nombre del producto N°{x+1}: ")
        nombres.append(n)
        p=int(input(f"Ingrese el precio de {n}: "))
        precios.append(p)
    return[nombres,precios]

def mostar(nombres,precios):
    print("---LISTA DE LOS NOMBRES Y LOS PRECIOS---")
    for x in range(5):
        print(f"{nombres[x]}, {precios[x]}")
def mayor(nombres,precios):
    mami=nombres[0]
    mayor=precios[0]
    for x in range(1,len(precios)):
        if precios[x]>mayor:
            mayor=precios[x]
            mami=nombres[x]
    return mayor,mami
def pedir_nuevo_importe():
    nuevo=int(input("Ingrese el importe que deseé comparar con los precios: "))
    return nuevo
def comparar(nombres,precios,nuevo):
    print("---PRECIOS MENORES AL IMPORTE QUE INGRESO---")
    resultado=[]
    for x in range(len(precios)):
        if precios[x] <= nuevo:
            resultado.append((nombres[x], precios[x]))
    return resultado
nomb,produ=cargar()
mostar(nomb,produ)
precio, articulo=mayor(nomb,produ)
print("El mayor articulo es:", articulo, "con el precio de: ", precio)
nuevo=pedir_nuevo_importe()
resultado=comparar(nomb, produ, nuevo)
for articulo, precio in resultado:
    print(articulo, precio)

