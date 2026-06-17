"""
Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada
elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15.
"""
def cargar():
    productosyprecios=[]
    for x in range(5):
        p=input(f"Ingrese el nombre del producto N°{x+1}: ")
        pr=int(input(f"Ingrese el precio del producto elegido ({p}): "))
        productosyprecios.append((p,pr))
    return productosyprecios
def precios(productosyprecios):
    print("---PRODUCTOS ENTRE 10 Y 15---")
    for x in range(len(productosyprecios)):
        if 10 <= productosyprecios[x][1] <= 15:
            print([productosyprecios[x]]) 
def preciosos(productosyprecios):
    print("---LISTA DE PRODUCTOS Y PRECIOS---")
    for nombre,precio in productosyprecios:
        print([(nombre,precio)])

queque=cargar()
precios(queque)
preciosos(queque)
