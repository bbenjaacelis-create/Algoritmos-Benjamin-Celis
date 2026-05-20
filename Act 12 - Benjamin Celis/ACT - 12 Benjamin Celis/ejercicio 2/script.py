"""
2. Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la
altura promedio de las personas.
"""
n=int(input("Cuantas alturas queres ingresar?"))
for a in range(n):
    altura=float(input("Ingrese las alturas: "))
    ola = altura/n
print("Promedio...")
print(ola)