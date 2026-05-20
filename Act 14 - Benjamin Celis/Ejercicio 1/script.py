"""
1. Definir una lista que almacene por asignación los nombres de 5 personas.
Contar cuántos de esos nombres tienen 5 o más caracteres y mostrarlo.
"""
nombres=["Alfonso", "Mayta", "Victor", "Milei", "Luciano"]
contador = 0

for x in range(5):
    if len(nombres[x])>=5:
        contador=contador+1
    
print("La cantidad de nombres que tienen 5 o mas letras son:")
print(contador)