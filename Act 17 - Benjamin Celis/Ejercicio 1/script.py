"""
1. Se tiene la siguiente lista:
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
Imprimir la lista. Luego cambiar de elemento todos los enteros mayores a 50 del
primer elemento de &quot;lista&quot;. El resto de enteros menores a 50 deben encontrarse
en una nueva posición dentro de la lista.
Volver a imprimir la lista.
"""

lista = [[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

print("Lista original:")
print(lista)

menores = []

for k in range(len(lista)):
    posicion = 0
    while posicion < len(lista[k]):
        if lista[k][posicion] > 50:
            lista[0].append(lista[k][posicion])
            lista[k].pop(posicion)
        else:
            menores.append(lista[k][posicion])
            lista[k].pop(posicion)

lista.append(menores)

print("Lista modificada:")
print(lista)