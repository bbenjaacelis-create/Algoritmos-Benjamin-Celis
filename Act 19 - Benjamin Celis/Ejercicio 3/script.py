"""
3. Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos
debe retornar la suma de dichos valores. Debe tener tres parámetros por
defecto.
"""

def calcular_suma(n1, n2, n3=0, n4=0, n5=0):
    suma = n1 + n2 + n3 + n4 + n5
    return suma

def mostrar(resultado):
    print("--- RESULTADO ---")
    print(f"La suma es: {resultado}")

print("--- INGRESO DE DATOS ---")
v1 = int(input("Ingrese primer número: "))
v2 = int(input("Ingrese segundo número: "))
v3 = int(input("Ingrese tercer número: "))


total = calcular_suma(v1, v2, v3)

mostrar(total)