#5. Se ingresa por teclado un valor entero, mostrar una leyenda que indique si
#el número es positivo, negativo o nulo (es decir cero)

numero = int(input("Ingrese su numero"))
if numero > 0:
    print("Su numero es positivo")
elif numero < 0:
    print("Es negativo")
else:
    print("Es 0") 