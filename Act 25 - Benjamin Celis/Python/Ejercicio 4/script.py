"""
Un comercio de tecnología necesita administrar el stock de sus 5 componentes clave de
hardware.
 Crear una lista donde cada elemento sea una tupla de tres elementos que
represente: (nombre_articulo, precio, stock).
Desarrollar las siguientes funciones:
1. Cargar inventario: Ingresar por teclado los datos de los 5 componentes para
armar las tuplas correspondientes.
2. Imprimir listado: Mostrar por pantalla los nombres, precios y stock de todos los
artículos desempaquetando la tupla de manera directa en el bucle for.
3. Valor del Inventario: Calcular e informar el valor total de la mercadería en el local
(sumando el resultado de precio * stock de cada uno de los componentes).
4. Alerta de Reposición: Imprimir el nombre de todos aquellos artículos cuyo stock
sea menor o igual a 10 unidades para emitir un aviso de compra urgente.
"""
def cargar_inventario():
    inventario = []
    for i in range(5):
        nombre = input(f"Ingrese el nombre del articulo {i + 1}: ")
        precio = float(input(f"Ingrese el precio de {nombre}: "))
        stock = int(input(f"Ingrese el stock de {nombre}: "))
        inventario.append((nombre, precio, stock))
    return inventario

def imprimir_listado(inventario):
    print("--- LISTADO DE COMPONENTES ---")
    for nombre, precio, stock in inventario:
        print(f"Articulo: {nombre} | Precio: ${precio} | Stock: {stock} unidades")

def calcular_valor_inventario(inventario):
    total = 0.0
    for nombre, precio, stock in inventario:
        total = total + (precio * stock)
    return total

def obtener_alertas_reposicion(inventario):
    articulos_bajos = []
    for nombre, precio, stock in inventario:
        if stock <= 10:
            articulos_bajos.append(nombre)
    return articulos_bajos

def mostrar_valor_total(valor_total):
    print("--- VALOR TOTAL DEL INVENTARIO ---")
    print(f"El valor total de la mercaderia es: ${valor_total}")

def mostrar_alertas(alertas):
    print("--- ALERTA DE REPOSICION (URGENTE) ---")
    if len(alertas) == 0:
        print("No hay articulos con necesidad urgente de reposicion.")
    else:
        for nombre in alertas:
            print(f"AVISO: Stock bajo (<= 10 unidades) en articulo: {nombre}")

inventario = cargar_inventario()
imprimir_listado(inventario)
valor_total = calcular_valor_inventario(inventario)
mostrar_valor_total(valor_total)
alertas = obtener_alertas_reposicion(inventario)
mostrar_alertas(alertas)