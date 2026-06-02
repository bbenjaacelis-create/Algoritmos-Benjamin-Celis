"""
3. Confeccionar una función que calcule la superficie de un rectángulo y la
retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y
luego mostrar cuál de los dos tiene una superficie mayor.
"""
def retornar_superficie(lado1, lado2):
    superficie = lado1 * lado2
    return superficie
def pedir_datos():
    l1=int(input("Ingrese lado 1: "))
    l2=int(input("Ingrese lado 2: "))
    sup=retornar_superficie(l1,l2)
    return sup
def mostrar_mayor(sup1, sup2):
    if sup1>sup2:
        print("El lado 1 es mayor")
    elif sup2>sup1:
        print("El lado 2 es mayor")
    else:
        print("Ambos son iguales")

print("Rectangulo 1")
rectangulo1=pedir_datos()
print("Rectangulo 2")
rectangulo2=pedir_datos()
mostrar_mayor(rectangulo1,rectangulo2)