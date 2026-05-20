"""
Cargar por teclado y almacenar en una lista las alturas de 5 personas
(valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más
altas que el promedio y cuántas más bajas.
"""
alturas = []

for x in range(5):
    altura = float(input(f"Ingresar altura n°{x+1}:"))
    alturas.append(altura)

suma = 0

for x in range(5):
    suma = suma + alturas[x]

promedio = suma / 5

altos = 0
bajos = 0

for x in range(5):
    if alturas[x] > promedio:
        altos = altos + 1
    elif alturas[x] < promedio:
        bajos = bajos + 1

print("Lista de alturas:")
print(alturas)
print("Promedio:")
print(promedio)
print("Más altos que el promedio:")
print(altos)
print("Más bajos que el promedio:")
print(bajos)