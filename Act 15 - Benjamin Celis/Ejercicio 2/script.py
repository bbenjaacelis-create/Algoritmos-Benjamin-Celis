"""
2. Realizar un programa que pida la carga de dos listas numéricas enteras
de 4 elementos cada una. Generar una tercera lista que surja de la suma
de los elementos de la misma posición de cada lista. Mostrar esta tercera
lista.
"""
luno=[]
ldos=[]
ltres= []
for x in range(4):
    l1=int(input(f"Ingrese el {x+1}° valor para la primera lista: "))
    luno.append(l1)
for x in range(4):
    l2=int(input(f"Ingrese el {x+1}° valor para la segunda lista: "))
    ldos.append(l2)
for x in range(4):
    suma_posicion = luno[x] + ldos[x]
    ltres.append(suma_posicion)
print(f"Primera lista: {luno}")
print(f"Segunda lista: {ldos}")
print(f"Tercera lista: {ltres}")