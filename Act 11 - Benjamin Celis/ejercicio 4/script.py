#4. Se ingresa por teclado un número positivo de uno o dos dígitos (1..99)
#mostrar un mensaje indicando si el número tiene uno o dos dígitos.
#(Tener en cuenta que condición debe cumplirse para tener dos dígitos un
#número entero)

digito = int(input("Ingrese su digito..."))
if digito < 9:
    print("Su digito tiene un solo digito")
else:
    print("Su digito tiene dos digitos")