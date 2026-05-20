"""
4. Se realiza la carga de 10 valores enteros por teclado.
Se desea conocer:
a. La cantidad de valores ingresados negativos.
b. La cantidad de valores ingresados positivos.
c. La cantidad de múltiplos de 15.
d. El valor acumulado de los números ingresados que son pares.
"""
negativos = 0
positivos = 0
multiplos = 0
suma = 0
for a in range (1, 11):
    valores = int(input("Ingrese 10 valores: "))
    if valores > 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1
    if valores%15 == 0:
        multiplos = multiplos + 1
    if valores%2 == 0:
        suma = suma + valores
print(f"Cantidad de valores negativos: {negativos}")
print(f"Cantidad de valores positivos: {positivos}")
print(f"Cantidad de multiplos de 15 {multiplos}")
print(f"Suma de los numeros ingresados que son pares: {suma}")