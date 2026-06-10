"""
Confeccionar una función que reciba una serie de edades y me retorne la
cantidad que son mayores o iguales a 18 (como mínimo se envía un entero
a la función)
"""
pedir=int(input("Cuantos usuarios desea saber si son mayores/menores?: "))
def pedir_datos(pedir):
    edades=[]
    for x in range(pedir):
        ed=int(input(f"Ingrese la edad del usuario {x+1}: "))
        edades.append(ed)
    return edades
def consultar(edades):
    contador=0
    for edad in edades:
        if edad>=18:
            contador=contador+1
    return contador
lista_edades = pedir_datos(pedir)
mayores_edad=consultar(lista_edades)
print("Los usuarios mayores a 18 son: ", mayores_edad)