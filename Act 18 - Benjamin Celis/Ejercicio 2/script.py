"""
2. Confeccionar una función que reciba tres enteros y los muestre ordenados
de menor a mayor. En otra función solicitar la carga de 3 enteros por
teclado y proceder a llamar a la primer función definida.
"""

def ordenar_y_mostrar(a, b, c):
    if a <= b and a <= c:
        if b <= c:
            print(f"El orden es: {a}, {b}, {c}")
        else:
            print(f"El orden es: {a}, {c}, {b}")
    elif b <= a and b <= c:
        if a <= c:
            print(f"El orden es: {b}, {a}, {c}")
        else:
            print(f"El orden es: {b}, {c}, {a}")
    else: 
        if a <= b:
            print(f"El orden es: {c}, {a}, {b}")
        else:
            print(f"El orden es: {c}, {b}, {a}")


def cargar_datos():
    print("--- Carga de Números ---")
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))
    num3 = int(input("Ingrese el tercer número entero: "))
    ordenar_y_mostrar(num1, num2, num3)


cargar_datos()