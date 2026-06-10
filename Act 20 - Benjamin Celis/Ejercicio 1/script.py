"""
Desarrollar una función que reciba una lista de string y nos retorne el que
tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres
debe retornar el que tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string:
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres",mascaracteres(palabras))

(La lista debe tener la misma cantidad de elementos, pero los textos los
eligen ustedes)
"""

def cargar():
    lista=[]
    for x in range (6):
        l=input(f"Ingrese el texto {x+1}: ")
        lista.append(l)
    return lista
def calcular(lista):
    mayor=lista[0]
    for x in range(1,len(lista)):
        if len(lista[x])>len(mayor):
            mayor=lista[x]
        if len(lista[x])== len(mayor) and lista[x]<mayor:
            mayor=lista[x]
    return mayor

palabras = cargar()
print("Palabra con más caracteres:", calcular(palabras))