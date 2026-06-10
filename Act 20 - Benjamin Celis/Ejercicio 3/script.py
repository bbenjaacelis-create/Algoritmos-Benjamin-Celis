"""
Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores
positivos y en otra los negativos.
3) Imprimir las dos listas generadas.
"""
def lista_uno():
    lista_uno=[]
    for x in range(10):
        l1=int(input(f"Ingrese el valor N°{x+1}: "))
        lista_uno.append(l1)
    return lista_uno
def divlistas(lista_uno):
    pos=[]
    nega=[]
    for x in range(len(lista_uno)):
        if lista_uno[x]>0:
            pos.append(lista_uno[x])
        else:
            nega.append(lista_uno[x])
    return pos,nega
def mostrar(pos,nega):
    print("---LISTAS POSITIVAS/NEGATIVAS---")
    print(pos,nega)
cargarlista=lista_uno()
lista1,lista2=divlistas(cargarlista)
mostrar(lista1, lista2)