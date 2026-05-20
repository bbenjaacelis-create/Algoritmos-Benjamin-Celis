#1. Realizar un programa que lea cuatro valores numéricos e 
#informar su suma y promedio.

numero1 = int(input("Ingrese 1 numeros"))
numero2 = int(input("Ingrese 2 numeros"))
numero3 = int(input("Ingrese 3 numeros"))
numero4 = int(input("Ingrese 4 numeros"))
suma = numero1 + numero2 + numero3 + numero4
promedio = suma / 4
print (f"Su suma es: {suma}")
print (f"Su promedio es: {promedio}")