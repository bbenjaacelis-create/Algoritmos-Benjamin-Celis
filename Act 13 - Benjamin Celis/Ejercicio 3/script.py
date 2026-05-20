"""
3. Realizar un programa que permita cargar dos listas de 15 valores cada una.
Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor
(mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales") Tener en cuenta que
puede haber dos o más estructuras repetitivas en un algoritmo.
"""
suma1 = 0
suma2 = 0
for a in range (1, 16):
    valor1 = int(input(f"Ingrese valores {a} de la lista 1"))
    suma1 = suma1 + valor1
for b in range (1, 16):
    valor2 = int(input(f"Ingrese valores {b} de la lista 2"))
    suma2 = suma2 + valor2
if suma1 > suma2:
    print("Lista 1 mayor")
elif suma2 > suma1:
    print("Lista 2 mayor")
else:
    print("Listas iguales")