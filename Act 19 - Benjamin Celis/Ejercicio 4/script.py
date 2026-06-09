"""
4. Elaborar una función que muestre la tabla de multiplicar del valor que le
enviemos como parámetro. Definir un segundo parámetro llamado termino
que por defecto almacene el valor 10. Se deben mostrar tantos términos de
la tabla de multiplicar como lo indica el segundo parámetro.
Llamar a la función desde el bloque principal de nuestro programa con
argumentos nombrados.
"""
def calcular(pe):
    for x in range(1,13):
        print(f"{pe} x {x} = {pe*x}")
        print("----------")

def mostrar(pe):
   print("---Resultado---")
   calcular(pe)

def ingresar():
    print("----INGRESO DE LOS DATOS----")
    pe=int(input("Ingrese el numero por el cual quieres saber su tabla: "))
    return pe

numero = ingresar()
mostrar(numero)