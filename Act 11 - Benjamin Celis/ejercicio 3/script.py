#3. Realizar un programa que solicite la carga por teclado de dos números, si el
#primero es mayor al segundo informar su suma y diferencia, en caso
#contrario informar el producto y la división del primero respecto al segundo.

carga1 = float(input("INGRESE SU PRIMERA CARGA: "))
carga2 = float(input("INGRESE SU SEGUNDA CARGA: "))
suma = carga1 + carga2
diferencia = carga2 - carga1
producto = carga1 * carga2
division = carga1 / carga2
if carga1 > carga2:
    print(f"Su suma es: {suma}")
    print(f"Y su diferencia es: {diferencia}")
else:
    print(f"Su producto es {producto}")
    print(f"Su division es {division}")

