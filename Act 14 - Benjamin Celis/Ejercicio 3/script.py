"""
Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje
si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o
más posiciones en la lista)
"""
lista=[]

for x in range(5):
    elemento=int(input(f"Ingresar el elemento n°{x+1}:"))
    lista.append(elemento)

mayor = lista[0]

for x in range(1,5):
    if lista[x] > mayor:
        mayor = lista[x]

cantidad = 0

for x in range(5):
    if lista[x] == mayor:
        cantidad = cantidad + 1

print("Lista completa")
print(lista)
print("El elemento mayor es:")
print(mayor)

if cantidad >= 2:
    print("El número mayor se repite")
else:
    print("El número mayor no se repite")