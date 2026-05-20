"""
Se registran los nombres de 5 atletas y sus tiempos (en segundos) en una
carrera de 100 metros. El programa debe cargar los datos en dos vectores
paralelos, calcular y mostrar el promedio de los tiempos, mostrar el nombre del
atleta con mejor y peor tiempo, y mostrar los nombres de quienes superaron el
promedio.
"""
nombres=[]
tiempos=[]
suma_tiempos=0
for x in range(5):
    n=input(f"Ingrese el nombre del atleta N°{x+1}: ")
    nombres.append(n)
    t=float(input(f"Ingrese el tiempo del atleta {n}: "))
    tiempos.append(t)
print("---PROMEDIOS---")
for x in range(5):
    suma_tiempos=suma_tiempos+tiempos[x]
    promedio=suma_tiempos/5
print(f"promedio de {promedio}")
for x in range(4):
    for u in range(4-x):
        if tiempos[u]>tiempos[u+1]:
            aux1=tiempos[u]
            tiempos[u]=tiempos[u+1]
            tiempos[u+1]=aux1
            aux2=nombres[u]
            nombres[u]=nombres[u+1]
            nombres[u+1]=aux2
print("---LISTA DEL MEJOR AL PEOR PROMEDIO DE CADA PARTICIPANTE---")
for x in range(5):
    print(nombres[x],tiempos[x])
for x in range(5):
    if tiempos[x]>promedio:
        print(f"Participantes que superaron el promedio: {nombres[x]}")
print(F"El atleta con mejor tiempo fue: {nombres[0]}, con el tiempo de: {tiempos[0]}")
print(F"El atleta con peor tiempo fue: {nombres[4]}, con el tiempo de: {tiempos[4]}")