"""
Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
"""
def cargar():
    lista = []
    for x in range(5):
        ola = int(input(f"Carga el entero {x+1}: "))
        lista.append(ola)
    return lista


def convertibilidad(lista):
    mayor = lista[0]
    menor = lista[0]
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
        if elemento < menor:
            menor = elemento
    return (mayor, menor)


def imprimir(tupla):
    mayor, menor = tupla
    print("Mayor:", mayor)
    print("Menor:", menor)


listita = cargar()
resultado = convertibilidad(listita)
imprimir(resultado)