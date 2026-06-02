"""
1. Desarrollar un programa que solicite la carga de tres valores y muestre el
menor. Desde el bloque principal del programa llamar 2 veces a dicha
función (sin utilizar una estructura repetitiva)
"""
def mostrar_menor(v1,v2,v3):
    print("El menor de los numeros es: ")
    if v1<v2 and v1<v3:
        print(v1)
    else:
        if v2<v3:
            print(v2)
        else:
            print(v3)

def pedir():
    valor1=int(input("Ingrese su valor 1: "))
    valor2=int(input("Ingrese su valor 1: "))
    valor3=int(input("Ingrese su valor 1: "))
    mostrar_menor(valor1, valor2, valor3)

pedir()
pedir()